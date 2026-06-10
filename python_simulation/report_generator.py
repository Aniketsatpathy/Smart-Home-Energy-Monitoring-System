import pandas as pd


def generate_daily_report():

    df = pd.read_csv(
        "data/energy_log.csv"
    )

    df.to_csv(
        "outputs/daily_report.csv",
        index=False
    )

    print(
        "Daily Report Generated"
    )