# Smart Energy SAP Billing

![Python CI](https://github.com/JojoMab/smart-energy-sap-billing/actions/workflows/python-ci.yml/badge.svg)

Dieses Bewerberprojekt simuliert eine ERP-nahe Billing-Simulation für Energieverbrauchsdaten. Es zeigt SAP-nahe Prozesslogik, Tarifberechnung, Verbrauchsanalyse, CO2-Auswertung und eine einfache Prognose auf Basis synthetischer Daten.

## Bewerbungskontext

Das Projekt passt zu Wirtschaftsinformatik, Energie-IT und ERP-nahen Studiengängen. Es ist relevant für MONTANA Energie, Siemens Energy, Infineon und Cpro Conlog.

## Tech Stack

- Python 3.11
- CSV-Verarbeitung
- Tariflogik
- CO2-Auswertung
- Unit Tests
- GitHub Actions

## Funktionen

- Kundentypen HOUSEHOLD, BUSINESS und INDUSTRIAL verarbeiten
- Monatsverbräuche auswerten
- Grundpreis, Arbeitspreis und Steuern berechnen
- CO2-Werte mit Faktor 0,233 kg/kWh berechnen
- einfache Prognose über gleitenden Durchschnitt erzeugen

## Projektstruktur

```txt
smart-energy-sap-billing/
├── main.py
├── src/billing.py
├── src/energy_report.py
├── src/forecast.py
├── data/customer_data.csv
├── data/consumption_data.csv
├── tests/
└── docs/
```

## Schnellstart

```bash
python main.py
```

## Tests

```bash
python -m unittest discover -s tests -v
```

## Beispielausgabe

```txt
ERP-nahe Billing-Simulation abgeschlossen.
Familie Weber: letzte Rechnung 166.66 EUR, CO2 1123.73 kg, Prognose 438.33 kWh
```

## Hinweis auf synthetische Daten

Alle Kunden- und Verbrauchsdaten sind synthetisch. Das Projekt ist eine SAP-nahe Prozesslogik und keine Abbildung realer SAP-Landschaften.

## English Summary

This project simulates an ERP-related energy billing workflow with synthetic smart meter data. It demonstrates tariff logic, CO2 reporting, forecasting and testable Python modules.
