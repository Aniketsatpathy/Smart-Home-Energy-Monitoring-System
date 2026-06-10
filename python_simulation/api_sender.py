import requests


API_URL = (
    "http://127.0.0.1:8000/api/readings"
)


def send_reading(data):

    try:

        response = requests.post(
            API_URL,
            json=data
        )

        return response.status_code

    except Exception as e:

        print(
            "Connection Error:",
            e
        )

        return None