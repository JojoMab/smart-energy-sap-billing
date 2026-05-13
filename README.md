# Smart Energy SAP Billing System

Dieses Projekt kombiniert einen Smart-Meter-Analyzer mit einem SAP-nahen Billing-Prozess.

## Ziel

Das System liest Smart-Meter-Daten ein, analysiert Verbrauch und Erzeugung, erstellt einen Energiebericht und generiert anschließend automatisch eine Kundenrechnung.

## Bezug zur Praxis

Das Projekt simuliert einen digitalen Prozess aus der Energiewirtschaft:

1. Messdaten werden vom Smart Meter geliefert.
2. Die Daten werden analysiert.
3. Netzbezug und Einspeisung werden berechnet.
4. Ein Report wird erstellt.
5. Das Billing-System erstellt daraus eine Rechnung.

## Projektstruktur

```txt
smart-energy-sap-billing/
├── main.py
├── data/
│   ├── customers.csv
│   └── meter_data.csv
├── reports/
├── invoices/
└── src/
    ├── data_loader.py
    ├── analyzer.py
    ├── billing.py
    └── report_writer.py
```

## Ausführen

```bash
python main.py
```

## Beispielausgabe

```txt
Report erstellt: reports/smart_meter_report_C001.txt
Rechnung erstellt: invoices/invoice_C001_2026-05-02.txt
```

## Funktionen

- Kundendaten einlesen
- Smart-Meter-Daten einlesen
- Verbrauch und Erzeugung berechnen
- Netzbezug und Einspeisung berechnen
- Lastspitzen erkennen
- Monatsbilanz erstellen
- Verbrauchsprognose erstellen
- Rechnung mit Einspeisevergütung generieren

## Bewerbungssatz

Ich habe ein SAP-nahes Smart Energy Billing System entwickelt, das Smart-Meter-Daten verarbeitet, Energieberichte erstellt und daraus automatisch Kundenrechnungen generiert. Das Projekt verbindet Informatik, Energiewirtschaft, Datenanalyse und ERP-nahe Geschäftsprozesse.
