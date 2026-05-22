from src.report_writer import (
    build_billing_report,
    read_billing_report,
    write_billing_report,
)


def test_billing_report_uses_latest_consumption_and_summary_values():
    customers = [
        {
            "customer_id": "E001",
            "customer_name": "Familie Weber",
            "customer_type": "HOUSEHOLD",
        }
    ]
    consumption_rows = [
        {"customer_id": "E001", "month": "2026-01", "kwh": "100"},
        {"customer_id": "E001", "month": "2026-02", "kwh": "200"},
    ]

    report_rows = build_billing_report(customers, consumption_rows)

    assert report_rows == [
        {
            "customer_id": "E001",
            "customer_name": "Familie Weber",
            "customer_type": "HOUSEHOLD",
            "billing_month": "2026-02",
            "latest_kwh": "200.00",
            "annual_kwh": "300.00",
            "invoice_amount_eur": "90.44",
            "co2_kg": "69.90",
            "forecast_next_month_kwh": "150.00",
        }
    ]


def test_write_and_read_billing_report(tmp_path):
    report_rows = [
        {
            "customer_id": "E001",
            "customer_name": "Familie Weber",
            "customer_type": "HOUSEHOLD",
            "billing_month": "2026-02",
            "latest_kwh": "200.00",
            "annual_kwh": "300.00",
            "invoice_amount_eur": "90.44",
            "co2_kg": "69.90",
            "forecast_next_month_kwh": "150.00",
        }
    ]
    report_path = tmp_path / "billing_report.csv"

    write_billing_report(report_rows, report_path)

    assert read_billing_report(report_path) == report_rows
