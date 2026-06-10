# mqtt/metrics.py

from datetime import datetime

mqtt_metrics = {
    "messages_received": 0,
    "last_message_time": None,
    "broker_connected": False,
    "subscriber_started": datetime.now(),
}
