import csv
from datetime import datetime


def load_customers(path):
    customers = {}
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers[row['customer_id']] = {
                'customer_id': row['customer_id'],
                'name': row['name'],
                'address': row['address'],
                'tariff': float(row['tariff_eur_per_kwh']),
                'feed_in_tariff': float(row['feed_in_eur_per_kwh'])
            }
    return customers


def load_meter_data(path):
    data = []
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'timestamp': datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M'),
                'customer_id': row['customer_id'],
                'consumption': float(row['consumption_kwh']),
                'production': float(row['production_kwh'])
            })
    return data
