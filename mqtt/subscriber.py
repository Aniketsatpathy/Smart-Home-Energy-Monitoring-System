# mqtt/subscriber.py

import json
import os
import sys
import time
import requests

# ==================================================
# Project Path Configuration
# ==================================================
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

# pyrefly: ignore [missing-import]
import paho.mqtt.client as mqtt

# ==================================================
# Backend Imports
# ==================================================
from backend.database import SessionLocal
from backend.metrics_crud import update_message_metrics

# ==================================================
# MQTT Configuration
# ==================================================
MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "smart_home_energy"

# ==================================================
# FastAPI Configuration
# ==================================================
API_URL = "http://127.0.0.1:8000/api/readings"

# ==================================================
# Runtime Metrics
# ==================================================
messages_received = 0
start_time = time.time()
energy_total = 0.0
last_timestamp = None

# ==================================================
# MQTT Callbacks
# ==================================================

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("\n✅ MQTT Connected Successfully")
        client.subscribe(MQTT_TOPIC)
        print(f"📡 Subscribed to: {MQTT_TOPIC}")
    else:
        print(f"❌ MQTT Connection Failed: {rc}")


def on_message(client, userdata, msg):
    global messages_received
    global energy_total
    global last_timestamp

    db = None

    try:
        payload = json.loads(msg.payload.decode())

        voltage = float(payload.get("voltage", 0))
        current = float(payload.get("current", 0))
        power = float(payload.get("power", 0))

        # ==========================================
        # Derived Metrics
        # ==========================================
        current_time = time.time()

        if last_timestamp is None:
            interval_seconds = 5.0
        else:
            interval_seconds = current_time - last_timestamp

        last_timestamp = current_time

        energy_increment = (power * interval_seconds) / 3600000.0
        energy_total += energy_increment

        energy = round(energy_total, 6)
        cost = round(energy_total * 8, 2)
        appliance = "ESP32 Device"

        # ==========================================
        # Alert Logic
        # ==========================================
        if power >= 1800:
            alert = "OVERLOAD"
        elif power >= 1500:
            alert = "HIGH"
        elif power >= 1200:
            alert = "WARNING"
        else:
            alert = "NORMAL"

        # ==========================================
        # Payload For FastAPI
        # ==========================================
        api_payload = {
            "voltage": voltage,
            "current": current,
            "power": power,
            "energy": energy,
            "cost": cost,
            "appliance": appliance,
            "alert": alert,
        }

        # ==========================================
        # Send To Backend
        # ==========================================
        response = requests.post(
            API_URL,
            json=api_payload,
            timeout=5,
        )

        if response.status_code != 200:
            print(f"❌ FastAPI Error: {response.status_code}")
            return

        # ==========================================
        # Update Device Metrics
        # ==========================================
        db = SessionLocal()
        update_message_metrics(db)

        messages_received += 1

        print("\n================================")
        print(f"📨 Message #{messages_received}")
        print(f"Voltage : {voltage:.2f} V")
        print(f"Current : {current:.2f} A")
        print(f"Power   : {power:.2f} W")
        print(f"Energy  : {energy:.4f} kWh")
        print(f"Cost    : ₹ {cost:.2f}")
        print(f"Alert   : {alert}")
        print(f"API Status: {response.status_code}")
        print("================================")

    except Exception as e:
        print(f"\n❌ Subscriber Error: {e}")

    finally:
        if db:
            db.close()


# ==================================================
# MQTT Client Setup
# ==================================================
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("\n🚀 Starting MQTT Subscriber...")
print(f"Broker : {MQTT_BROKER}")
print(f"Topic  : {MQTT_TOPIC}")

try:
    client.connect(
        MQTT_BROKER,
        MQTT_PORT,
        60,
    )
    client.loop_forever()
except KeyboardInterrupt:
    print("\n🛑 Subscriber Stopped")
except Exception as e:
    print(f"\n❌ MQTT Startup Error: {e}")
