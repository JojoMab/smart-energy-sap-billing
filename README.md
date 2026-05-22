![Python CI](https://github.com/JojoMab/smart-energy-billing-analyzer/actions/workflows/python-ci.yml/badge.svg)

# Smart Energy Billing Analyzer

Dieses Bewerberprojekt analysiert synthetische Smart-Meter-Verbrauchs- und Abrechnungsdaten mit Python. Es zeigt eine nachvollziehbare Pipeline von CSV-Verbrauchsdaten über einen strukturierten Billing-Report bis zu automatisch erzeugten Rechnungen.

## Bewerbungskontext

Das Projekt ist als Portfolioarbeit für Bewerbungen im Bereich Wirtschaftsinformatik, Energie-IT, datenorientierte Softwareentwicklung und technische Analyse gedacht. Es zeigt, wie Verbrauchsdaten strukturiert eingelesen, fachlich ausgewertet und mit Tests abgesichert werden können.

## Tech Stack

- Python 3.11
- CSV-Verarbeitung
- Tariflogik
- CO2-Auswertung
- einfache Verbrauchsprognose
- Billing-Report als CSV
- Rechnungserzeugung aus dem Report
- Unit Tests
- GitHub Actions

## Funktionen

- Kundentypen HOUSEHOLD, BUSINESS und INDUSTRIAL verarbeiten
- Monatsverbräuche auswerten
- Grundpreis, Arbeitspreis und Steuern berechnen
- CO2-Werte mit Faktor 0,233 kg/kWh berechnen
- einfache Prognose über gleitenden Durchschnitt erzeugen
- `reports/billing_report.csv` als fachliche Zwischenstufe erzeugen
- Rechnungen pro Kunde aus dem Billing-Report in `invoices/` speichern
- Beispielausgabe für Recruiter und technische Prüfer bereitstellen

## Projektstruktur

```txt
smart-energy-billing-analyzer/
├── main.py
├── data/
│   ├── customer_data.csv
│   └── consumption_data.csv
├── docs/
│   ├── application_fit.md
│   └── recruiter_summary_de.md
├── examples/
│   ├── README.md
│   └── terminal_output.txt
├── invoices/
├── reports/
├── tests/
├── src/
│   ├── billing.py
│   ├── energy_report.py
│   ├── forecast.py
│   ├── invoice_writer.py
│   └── report_writer.py
├── requirements.txt
└── .gitignore
```

## Ablauf

```txt
CSV-Verbrauchsdaten
→ Billing-Report unter reports/billing_report.csv
→ Rechnungen pro Kunde unter invoices/
```

## Schnellstart

```bash
python -m pip install -r requirements.txt
python main.py
```

## Tests ausführen

```bash
python -m pytest tests/ -v
```

## Beispielausgabe

```txt
Energy-Billing-Auswertung abgeschlossen.
Billing-Report in reports/billing_report.csv gespeichert.
Familie Weber: letzte Rechnung 158.98 EUR, CO2 1209.27 kg, Prognose 438.33 kWh
Bäckerei Klein: letzte Rechnung 462.91 EUR, CO2 3641.79 kg, Prognose 1308.33 kWh
Metallbau Süd: letzte Rechnung 1930.18 EUR, CO2 18041.19 kg, Prognose 6458.33 kWh
3 Rechnungen aus Billing-Report in invoices/ gespeichert.
```

## Hinweis auf synthetische Daten

Alle Daten sind synthetisch und dienen ausschließlich der Demonstration.

Dieses Projekt ist ein Bewerberprojekt und nicht für den produktiven Einsatz vorgesehen.

## English Summary

This applicant project analyzes synthetic energy consumption and billing data with Python. It demonstrates a CSV-to-report-to-invoice pipeline, tariff logic, CO2 reporting, a simple moving-average forecast and automated tests.
