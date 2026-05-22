from src.invoice_writer import build_invoice_text, write_invoices_from_report


def test_invoice_uses_report_values():
    report_row = {
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

    invoice_text = build_invoice_text(report_row)

    assert "Abrechnungsmonat: 2026-02" in invoice_text
    assert "Verbrauch: 200.00 kWh" in invoice_text
    assert "Rechnungsbetrag brutto: 90.44 EUR" in invoice_text
    assert "Jahresverbrauch im Report: 300.00 kWh" in invoice_text


def test_write_invoices_creates_invoice_file(tmp_path):
    report_rows = [
        {
            "customer_id": "E001",
            "customer_name": "Familie Weber",
            "customer_type": "HOUSEHOLD",
            "billing_month": "2026-01",
            "latest_kwh": "100.00",
            "annual_kwh": "100.00",
            "invoice_amount_eur": "52.36",
            "co2_kg": "23.30",
            "forecast_next_month_kwh": "100.00",
        }
    ]

    invoice_paths = write_invoices_from_report(report_rows, tmp_path)

    assert len(invoice_paths) == 1
    assert invoice_paths[0].name == "E001_2026-01_invoice.txt"
    assert "Verbrauch: 100.00 kWh" in invoice_paths[0].read_text(encoding="utf-8")
