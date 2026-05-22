import csv
from pathlib import Path

from src.billing import calculate_bill
from src.energy_report import calculate_co2
from src.forecast import moving_average_forecast


REPORT_FIELDS = [
    "customer_id",
    "customer_name",
    "customer_type",
    "billing_month",
    "latest_kwh",
    "annual_kwh",
    "invoice_amount_eur",
    "co2_kg",
    "forecast_next_month_kwh",
]


def customer_consumption_rows(customer_id, consumption_rows):
    return sorted(
        [row for row in consumption_rows if row["customer_id"] == customer_id],
        key=lambda row: row["month"],
    )


def build_billing_report_row(customer, consumption_rows):
    rows = customer_consumption_rows(customer["customer_id"], consumption_rows)
    if not rows:
        raise ValueError(f"No consumption data found for customer {customer['customer_id']}")

    values = [float(row["kwh"]) for row in rows]
    latest_row = rows[-1]
    latest_kwh = float(latest_row["kwh"])
    annual_kwh = sum(values)

    return {
        "customer_id": customer["customer_id"],
        "customer_name": customer["customer_name"],
        "customer_type": customer["customer_type"],
        "billing_month": latest_row["month"],
        "latest_kwh": f"{latest_kwh:.2f}",
        "annual_kwh": f"{annual_kwh:.2f}",
        "invoice_amount_eur": f"{calculate_bill(customer['customer_type'], latest_kwh):.2f}",
        "co2_kg": f"{calculate_co2(annual_kwh):.2f}",
        "forecast_next_month_kwh": f"{moving_average_forecast(values):.2f}",
    }


def build_billing_report(customers, consumption_rows):
    return [
        build_billing_report_row(customer, consumption_rows)
        for customer in customers
    ]


def write_billing_report(report_rows, output_path="reports/billing_report.csv"):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=REPORT_FIELDS)
        writer.writeheader()
        writer.writerows(report_rows)

    return path


def read_billing_report(path="reports/billing_report.csv"):
    with Path(path).open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))
