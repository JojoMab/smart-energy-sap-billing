import os
from datetime import date


def write_energy_report(customer, analysis, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"smart_meter_report_{customer['customer_id']}.txt")

    with open(filename, 'w', encoding='utf-8') as file:
        file.write('Smart Meter Energy Report\n')
        file.write('=========================\n\n')
        file.write(f"Customer ID: {customer['customer_id']}\n")
        file.write(f"Name: {customer['name']}\n\n")
        file.write(f"Total consumption: {analysis['total_consumption']:.2f} kWh\n")
        file.write(f"Total production: {analysis['total_production']:.2f} kWh\n")
        file.write(f"Grid usage: {analysis['grid_usage']:.2f} kWh\n")
        file.write(f"Feed-in: {analysis['feed_in']:.2f} kWh\n")
        file.write(f"Next-month forecast: {analysis['forecast_month']:.2f} kWh\n\n")

        file.write('Monthly balance:\n')
        for month, values in analysis['monthly'].items():
            balance = values['production'] - values['consumption']
            file.write(f"{month}: consumption {values['consumption']:.2f} kWh, production {values['production']:.2f} kWh, balance {balance:.2f} kWh\n")

        file.write('\nPeak loads:\n')
        if analysis['peaks']:
            for peak in analysis['peaks']:
                file.write(f"{peak['timestamp']} - {peak['consumption']:.2f} kWh\n")
        else:
            file.write('No peak loads detected.\n')

    return filename


def write_invoice(customer, analysis, bill, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"invoice_{customer['customer_id']}_{date.today()}.txt")

    with open(filename, 'w', encoding='utf-8') as file:
        file.write('Smart Energy SAP-like Invoice\n')
        file.write('=============================\n\n')
        file.write(f"Invoice date: {date.today()}\n")
        file.write(f"Customer ID: {customer['customer_id']}\n")
        file.write(f"Name: {customer['name']}\n")
        file.write(f"Address: {customer['address']}\n\n")

        file.write('Meter data:\n')
        file.write(f"Total consumption: {analysis['total_consumption']:.2f} kWh\n")
        file.write(f"Total production: {analysis['total_production']:.2f} kWh\n")
        file.write(f"Grid usage: {analysis['grid_usage']:.2f} kWh\n")
        file.write(f"Feed-in: {analysis['feed_in']:.2f} kWh\n\n")

        file.write('Billing:\n')
        file.write(f"Energy tariff: {customer['tariff']:.2f} EUR/kWh\n")
        file.write(f"Feed-in tariff: {customer['feed_in_tariff']:.2f} EUR/kWh\n")
        file.write(f"Energy cost: {bill['energy_cost']:.2f} EUR\n")
        file.write(f"Feed-in credit: {bill['feed_in_credit']:.2f} EUR\n")
        file.write(f"Total amount: {bill['net_amount']:.2f} EUR\n")

    return filename
