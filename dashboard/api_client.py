# dashboard/api_client.py

import requests
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"


def get_all_readings():

    response = requests.get(f"{BASE_URL}/api/readings")

    data = response.json()

    # print("\nAPI RESPONSE:")
    # print(data)

    return pd.DataFrame(data)


def get_latest():

    response = requests.get(f"{BASE_URL}/api/latest")

    return response.json()


def get_stats():

    response = requests.get(f"{BASE_URL}/api/stats")

    return response.json()


def get_device_health():

    response = requests.get(f"{BASE_URL}/api/device-health")

    return response.json()


BASE_URL = "http://127.0.0.1:8000"


def get_system_health():

    try:

        response = requests.get(f"{BASE_URL}/api/system-health", timeout=5)

        if response.status_code != 200:

            return {
                "mqtt_connected": False,
                "messages_received": 0,
                "seconds_since_last_message": None,
                "uptime_seconds": 0,
            }

        return response.json()

    except Exception:

        return {
            "mqtt_connected": False,
            "messages_received": 0,
            "seconds_since_last_message": None,
            "uptime_seconds": 0,
        }
