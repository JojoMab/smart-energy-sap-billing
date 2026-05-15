import csv
from dataclasses import dataclass

@dataclass
class Reading:
    customer_type: str
    month: str
    kwh: float
    tariff_ct: float

def load_readings(path='data/energy_readings.csv'):
    with open(path, newline='', encoding='utf-8') as f:
        return [Reading(r['customer_type'], r['month'], float(r['kwh']), float(r['tariff_ct'])) for r in csv.DictReader(f)]

def monthly_cost(reading):
    return round(reading.kwh * reading.tariff_ct / 100, 2)

def co2_kg(reading):
    return round(reading.kwh * 0.38, 2)

def recommendation(reading):
    if reading.kwh > 900: return 'check efficiency potential'
    return 'regular consumption'

if __name__ == '__main__':
    total = sum(monthly_cost(r) for r in load_readings())
    print(f'Report generated successfully. Total cost EUR: {total:.2f}')
