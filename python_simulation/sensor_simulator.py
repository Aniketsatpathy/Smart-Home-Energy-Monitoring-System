import random


def get_voltage():

    return round(
        random.uniform(220, 240),
        2
    )


def get_current():

    return round(
        random.uniform(0.5, 10),
        2
    )


def get_appliance_status():

    appliances = [
        "Fan",
        "AC",
        "TV",
        "Laptop",
        "Refrigerator",
        "Washing Machine"
    ]

    return random.choice(appliances)