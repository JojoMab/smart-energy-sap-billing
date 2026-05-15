from collections import defaultdict

from src.data_loader import load_customers, load_meter_data
from src.analyzer import analyze_customer_energy
from src.billing import calculate_bill
from src.report_writer import write_energy_report, write_invoice

CUSTOMERS_FILE = 'data/customers.csv'
METER_DATA_FILE = 'data/meter_data.csv'
REPORT_DIR = 'reports'
INVOICE_DIR = 'invoices'


def group_by_customer(meter_data):
    grouped = defaultdict(list)
    for record in meter_data:
        grouped[record['customer_id']].append(record)
    return grouped


def main():
    customers = load_customers(CUSTOMERS_FILE)
    meter_data = load_meter_data(METER_DATA_FILE)
    grouped_data = group_by_customer(meter_data)

    for customer_id, records in grouped_data.items():
        if customer_id not in customers:
            print(f'Customer not found: {customer_id}')
            continue

        customer = customers[customer_id]
        analysis = analyze_customer_energy(records)
        bill = calculate_bill(customer, analysis)

        report_file = write_energy_report(customer, analysis, REPORT_DIR)
        invoice_file = write_invoice(customer, analysis, bill, INVOICE_DIR)

        print(f'Report created: {report_file}')
        print(f'Invoice created: {invoice_file}')
        print('-' * 40)


if __name__ == '__main__':
    main()
