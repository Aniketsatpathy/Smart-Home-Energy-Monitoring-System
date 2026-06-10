WARNING_LIMIT = 1500

HIGH_LIMIT = 2500

OVERLOAD_LIMIT = 5000


def get_alert(power):

    if power > OVERLOAD_LIMIT:
        return "OVERLOAD"

    elif power > HIGH_LIMIT:
        return "HIGH CONSUMPTION"

    elif power > WARNING_LIMIT:
        return "WARNING"

    return "NORMAL"