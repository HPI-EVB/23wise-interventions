from enum import Enum
from typing import Any

class RecordKey(Enum):
    temperature = 0
    pulse = 1
    blood_pressure = 2
    blood_sugar = 3
    blood_oxygen = 4
    sodium_plasma = 5
    potassium_plasma = 6
    hb = 7
    leucocytes = 8
    thrombocytes = 9
    quick_inr = 10
    aptt = 11

__record_abbreviations = {
    'Vit_Blutdruck': RecordKey.blood_pressure,
    'Vit_Puls': RecordKey.pulse,
    'Vit_Temperatur': RecordKey.temperature,
    'BZ_Kurve_02': RecordKey.blood_sugar,
    'Vit_Pulsoximetri': RecordKey.blood_oxygen,
    # 'PflANM_43': RecordKey.height,
    # 'statStill_009': RecordKey.height,
    # 'VZ_HNOGroesse': RecordKey.height,
    # 'PflANM_44': RecordKey.weight,
    # 'allgAnamn_139': RecordKey.planned_release,
}

def record_key_from_abbreviation(abbreviation: str):
    if abbreviation not in __record_abbreviations: return None
    return __record_abbreviations[abbreviation]

class Record:
    minutes_since_start: float
    value: Any

    def __init__(self, minutes_since_start: float, value: Any):
        self.minutes_since_start = minutes_since_start
        self.value = value

class Visit:
    records: dict[RecordKey, list[Record]]

    def __init__(self):
        self.records = {}

    def append(self, key: RecordKey, record: Record):
        if key in self.records:
            self.records[key].append(record)
        else:
            self.records[key] = [record]

class VisitData:
    visits: dict[str, Visit]

    def __init__(self):
        self.visits = {}

    def append(self, id: str, record_key: RecordKey, record: Record):
        if id in self.visits:
            self.visits[id].append(record_key, record)
        else:
            visit = Visit()
            visit.append(record_key, record)
            self.visits[id] = Visit()
