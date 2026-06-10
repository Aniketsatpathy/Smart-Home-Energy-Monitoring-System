import time

import os

import sys

# --------------------------------------------------
# Project Path Configuration
# --------------------------------------------------

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(PROJECT_ROOT)

from sensor_simulator import get_voltage, get_current, get_appliance_status

from calculations import calculate_power, calculate_energy, calculate_cost

from alert_engine import get_alert

from mqtt.publisher import publish_reading


total_energy = 0


print("\nSIMULATOR STARTED\n")


while True:

    voltage = get_voltage()

    current = get_current()

    appliance = get_appliance_status()

    power = calculate_power(voltage, current)

    total_energy = calculate_energy(power)

    cost = calculate_cost(total_energy)

    alert = "WARNING" if power > 1800 else "NORMAL"

    payload = {
        "voltage": voltage,
        "current": current,
        "power": round(power, 2),
        "energy": round(total_energy, 4),
        "cost": round(cost, 2),
        "appliance": appliance,
        "alert": alert,
    }

    publish_reading(payload)

    print(f"{appliance} | " f"{power:.2f}W | " f"{alert}")

    # CRITICAL
    time.sleep(5)
