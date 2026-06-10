from publisher import publish_reading

publish_reading(
    {
        "voltage": 230,
        "current": 3.1,
        "power": 713,
        "energy": 1.2,
        "cost": 9.6,
        "appliance": "Fan",
        "alert": "NORMAL",
    }
)

print("Message Published Successfully")
