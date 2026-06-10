from datetime import datetime

from .models import SystemMetrics


def initialize_metrics(db):

    metrics = db.query(SystemMetrics).first()

    if not metrics:

        metrics = SystemMetrics()

        db.add(metrics)

        db.commit()

        db.refresh(metrics)

    return metrics


def update_message_metrics(db):

    metrics = initialize_metrics(db)

    metrics.messages_received += 1

    metrics.last_message_time = datetime.utcnow()

    metrics.mqtt_connected = True

    db.commit()

    return metrics


def get_metrics(db):

    return initialize_metrics(db)
