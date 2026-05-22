import csv

from src.invoice_writer import write_invoices_from_report
from src.report_writer import (
    build_billing_report,
    read_billing_report,
    write_billing_report,
)


def load_csv(path):
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main():
    customers = load_csv("data/customer_data.csv")
    consumption = load_csv("data/consumption_data.csv")

    report_rows = build_billing_report(customers, consumption)
    report_path = write_billing_report(report_rows)
    invoice_paths = write_invoices_from_report(read_billing_report(report_path))

    print("Energy-Billing-Auswertung abgeschlossen.")
    print(f"Billing-Report in {report_path} gespeichert.")
    for row in report_rows:
        print(
            f"{row['customer_name']}: letzte Rechnung {float(row['invoice_amount_eur']):.2f} EUR, "
            f"CO2 {float(row['co2_kg']):.2f} kg, "
            f"Prognose {float(row['forecast_next_month_kwh']):.2f} kWh"
        )
    print(f"{len(invoice_paths)} Rechnungen aus Billing-Report in invoices/ gespeichert.")


if __name__ == "__main__":
    main()
