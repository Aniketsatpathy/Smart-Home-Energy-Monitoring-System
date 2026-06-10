RATE_PER_KWH = 8


def calculate_power(
    voltage,
    current
):

    return voltage * current


def calculate_energy(
    power,
    interval_seconds=5
):

    return (
        power *
        interval_seconds
    ) / (1000 * 3600)


def calculate_cost(
    total_energy
):

    return (
        total_energy *
        RATE_PER_KWH
    )