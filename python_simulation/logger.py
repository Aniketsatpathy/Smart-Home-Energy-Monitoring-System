import csv
import os


FILE_NAME = "data/energy_log.csv"


def initialize_logger():

    if not os.path.exists(FILE_NAME):

        with open(
            FILE_NAME,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Timestamp",
                "Voltage",
                "Current",
                "Power",
                "Energy",
                "Cost",
                "Appliance",
                "Alert"
            ])


def save_record(record):

    with open(
        FILE_NAME,
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(record)