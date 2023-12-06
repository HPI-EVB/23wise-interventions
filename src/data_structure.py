from datetime import date
from enum import Enum
from typing import Any


class RecordKey(Enum):
    temperature = 0
    pulse = 1
    blood_pressure = 2
    blood_sugar = 3
    sodium_plasma = 4
    potassium_plasma = 5
    hb = 6
    leucocytes = 7
    thrombocytes = 8
    quick_inr = 9
    aptt = 10

class Record:
    timestamp: date
    value: Any

class Visit:
    records: dict[RecordKey, list[Record]]
