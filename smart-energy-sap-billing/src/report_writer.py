import os
from datetime import date


def write_energy_report(customer, analysis, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"smart_meter_report_{customer['customer_id']}.txt")

    with open(filename, 'w', encoding='utf-8') as file:
        file.write('Smart Meter Energy Report\n')
        file.write('=========================\n\n')
        file.write(f"Kundennummer: {customer['customer_id']}\n")
        file.write(f"Name: {customer['name']}\n\n")
        file.write(f"Gesamtverbrauch: {analysis['total_consumption']:.2f} kWh\n")
        file.write(f"Gesamterzeugung: {analysis['total_production']:.2f} kWh\n")
        file.write(f"Netzbezug: {analysis['grid_usage']:.2f} kWh\n")
        file.write(f"Einspeisung: {analysis['feed_in']:.2f} kWh\n")
        file.write(f"Prognose nächster Monat: {analysis['forecast_month']:.2f} kWh\n\n")

        file.write('Monatliche Bilanz:\n')
        for month, values in analysis['monthly'].items():
            balance = values['production'] - values['consumption']
            file.write(f"{month}: Verbrauch {values['consumption']:.2f} kWh, Erzeugung {values['production']:.2f} kWh, Bilanz {balance:.2f} kWh\n")

        file.write('\nLastspitzen:\n')
        if analysis['peaks']:
            for peak in analysis['peaks']:
                file.write(f"{peak['timestamp']} - {peak['consumption']:.2f} kWh\n")
        else:
            file.write('Keine Lastspitzen erkannt.\n')

    return filename


def write_invoice(customer, analysis, bill, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"invoice_{customer['customer_id']}_{date.today()}.txt")

    with open(filename, 'w', encoding='utf-8') as file:
        file.write('Smart Energy SAP-like Invoice\n')
        file.write('=============================\n\n')
        file.write(f"Rechnungsdatum: {date.today()}\n")
        file.write(f"Kundennummer: {customer['customer_id']}\n")
        file.write(f"Name: {customer['name']}\n")
        file.write(f"Adresse: {customer['address']}\n\n")

        file.write('Messdaten:\n')
        file.write(f"Gesamtverbrauch: {analysis['total_consumption']:.2f} kWh\n")
        file.write(f"Gesamterzeugung: {analysis['total_production']:.2f} kWh\n")
        file.write(f"Netzbezug: {analysis['grid_usage']:.2f} kWh\n")
        file.write(f"Einspeisung: {analysis['feed_in']:.2f} kWh\n\n")

        file.write('Abrechnung:\n')
        file.write(f"Arbeitspreis: {customer['tariff']:.2f} EUR/kWh\n")
        file.write(f"Einspeisevergütung: {customer['feed_in_tariff']:.2f} EUR/kWh\n")
        file.write(f"Stromkosten: {bill['energy_cost']:.2f} EUR\n")
        file.write(f"Gutschrift Einspeisung: {bill['feed_in_credit']:.2f} EUR\n")
        file.write(f"Gesamtbetrag: {bill['net_amount']:.2f} EUR\n")

    return filename
