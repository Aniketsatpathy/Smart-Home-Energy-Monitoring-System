# backend/test_db.py

from .database import engine
from .database import SessionLocal

from .models import Base

from .crud import create_reading
from .crud import get_all_readings

Base.metadata.create_all(
    bind=engine
)

db = SessionLocal()

create_reading(
    db=db,
    voltage=230,
    current=2.5,
    power=575,
    energy=0.575,
    cost=4.6,
    appliance="Fan",
    alert="NORMAL"
)

readings = get_all_readings(db)

for row in readings:

    print(
        row.id,
        row.voltage,
        row.current,
        row.power,
        row.alert
    )

db.close()