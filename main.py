import time

from datetime import datetime

from python_simulation.sensor_simulator import (
    get_voltage,
    get_current,
    get_appliance_status
)

from python_simulation.calculations import (
    calculate_power,
    calculate_energy,
    calculate_cost
)

from python_simulation.alert_engine import (
    get_alert
)

from python_simulation.logger import (
    initialize_logger,
    save_record
)

initialize_logger()

total_energy = 0

print(
    "\nSMART HOME ENERGY MONITORING SYSTEM\n"
)

while True:

    voltage = get_voltage()

    current = get_current()

    appliance = get_appliance_status()

    power = calculate_power(
        voltage,
        current
    )

    energy = calculate_energy(
        power
    )

    total_energy += energy

    cost = calculate_cost(
        total_energy
    )

    alert = get_alert(
        power
    )

    timestamp = datetime.now()

    save_record([
        timestamp,
        round(voltage, 2),
        round(current, 2),
        round(power, 2),
        round(total_energy, 4),
        round(cost, 2),
        appliance,
        alert
    ])

    print(
        f"""
Time      : {timestamp}
Voltage   : {voltage} V
Current   : {current} A
Power     : {power:.2f} W
Energy    : {total_energy:.4f} kWh
Cost      : ₹{cost:.2f}
Appliance : {appliance}
Alert     : {alert}
"""
    )

    time.sleep(5)