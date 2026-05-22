from pathlib import Path


def build_invoice_text(report_row):
    return "\n".join(
        [
            "Smart Energy Billing Analyzer",
            "Rechnung auf Basis des Billing-Reports",
            "",
            f"Kunde: {report_row['customer_name']}",
            f"Kundennummer: {report_row['customer_id']}",
            f"Kundentyp: {report_row['customer_type']}",
            f"Abrechnungsmonat: {report_row['billing_month']}",
            f"Verbrauch: {float(report_row['latest_kwh']):.2f} kWh",
            f"Rechnungsbetrag brutto: {float(report_row['invoice_amount_eur']):.2f} EUR",
            "",
            f"Jahresverbrauch im Report: {float(report_row['annual_kwh']):.2f} kWh",
            f"CO2-Aequivalent: {float(report_row['co2_kg']):.2f} kg",
            f"Prognose naechster Monat: {float(report_row['forecast_next_month_kwh']):.2f} kWh",
            "",
            "Alle Daten sind synthetisch und dienen ausschliesslich der Demonstration.",
            "Dieses Projekt ist ein Bewerberprojekt und nicht fuer den produktiven Einsatz vorgesehen.",
            "",
        ]
    )


def write_invoice_from_report_row(report_row, output_dir="invoices"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    invoice_path = output_path / (
        f"{report_row['customer_id']}_{report_row['billing_month']}_invoice.txt"
    )
    invoice_path.write_text(build_invoice_text(report_row), encoding="utf-8")
    return invoice_path


def write_invoices_from_report(report_rows, output_dir="invoices"):
    return [
        write_invoice_from_report_row(report_row, output_dir)
        for report_row in report_rows
    ]
