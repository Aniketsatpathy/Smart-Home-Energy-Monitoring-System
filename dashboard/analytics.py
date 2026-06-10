# ============================================================
# analytics.py
#
# Analytics calculations used across dashboard
#
# ============================================================


def calculate_metrics(df):

    return {
        "max_power": float(df["power"].max()),
        "avg_power": float(df["power"].mean()),
        "total_energy": float(df["energy"].max()),
        "total_cost": float(df["cost"].max()),
        "total_records": len(df),
        "total_alerts": len(df[df["alert"] != "NORMAL"]),
    }
