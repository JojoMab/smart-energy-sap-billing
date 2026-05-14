# Smart Energy SAP Billing System

Smart Energy SAP Billing System ist ein Python-Projekt, das Smart-Meter-Daten analysiert und daraus automatisch Energieberichte und Kundenrechnungen erzeugt. Der Ablauf ist bewusst SAP- und ERP-nah aufgebaut: Messdaten werden eingelesen, betriebswirtschaftlich bewertet und in abrechenbare Dokumente überführt.

## GitHub-Beschreibung

Python-Projekt für Smart-Meter-Analyse und SAP-nahes Energy Billing mit automatischen Reports und Rechnungen.

## Kurzprofil für Recruiter

- Thema: Energiewirtschaft, Smart Metering, Billing und ERP-nahe Prozesse
- Technologie: Python, CSV-Verarbeitung, modulare Projektstruktur
- Eingabe: Kundendaten und Smart-Meter-Messwerte
- Ausgabe: Energieberichte und Rechnungen pro Kunde
- Fokus: Verbindung von technischer Datenanalyse und kaufmännischer Abrechnung

## Praxisnaher Ablauf

Das Projekt simuliert einen digitalen Prozess aus der Energiewirtschaft:

1. Smart Meter liefern Messdaten.
2. Das System liest Kunden- und Messdaten aus CSV-Dateien ein.
3. Verbrauch, Erzeugung, Netzbezug und Einspeisung werden berechnet.
4. Pro Kunde wird ein Energiebericht erstellt.
5. Aus den Analysewerten wird automatisch eine Rechnung mit Einspeisevergütung erzeugt.

## Funktionen

- Kundendaten einlesen
- Smart-Meter-Daten einlesen
- Verbrauch und Erzeugung berechnen
- Netzbezug und Einspeisung auswerten
- Lastspitzen erkennen
- Monatsbilanz erstellen
- Verbrauchsprognose ableiten
- Rechnung mit Einspeisevergütung generieren

## Schnellstart

Projekt aus dem Repository-Root starten:

```bash
python3 main.py
```

Erwartete Terminalausgabe:

```txt
Report erstellt: reports/smart_meter_report_C001.txt
Rechnung erstellt: invoices/invoice_C001_2026-05-14.txt
----------------------------------------
Report erstellt: reports/smart_meter_report_C002.txt
Rechnung erstellt: invoices/invoice_C002_2026-05-14.txt
----------------------------------------
Report erstellt: reports/smart_meter_report_C003.txt
Rechnung erstellt: invoices/invoice_C003_2026-05-14.txt
----------------------------------------
Report erstellt: reports/smart_meter_report_C004.txt
Rechnung erstellt: invoices/invoice_C004_2026-05-14.txt
----------------------------------------
Report erstellt: reports/smart_meter_report_C005.txt
Rechnung erstellt: invoices/invoice_C005_2026-05-14.txt
----------------------------------------
```

## Beispiele im Repository

Die Beispielausgaben sind bewusst versioniert, damit Recruiter das Ergebnis direkt auf GitHub prüfen können, ohne das Projekt lokal auszuführen:

- [Terminal-Mitschnitt](examples/terminal_output.txt)

Der Mitschnitt zeigt, welche Reports und Rechnungen beim Start für die Beispielkunden erzeugt werden.

## Projektstruktur

```txt
.
├── main.py
├── data/
│   ├── customers.csv
│   └── meter_data.csv
├── examples/
│   ├── README.md
│   └── terminal_output.txt
├── invoices/
├── reports/
└── src/
    ├── analyzer.py
    ├── billing.py
    ├── data_loader.py
    └── report_writer.py
```

## Eingabedaten

`data/customers.csv` enthält Kundendaten wie Tarif, Name und Kundennummer. `data/meter_data.csv` enthält die Messdaten je Kunde, zum Beispiel Verbrauch, Erzeugung und Zeitbezug.

## Ausgaben

Beim Start erzeugt das Programm pro Kunde:

- einen Energiebericht unter `reports/`
- eine Rechnung unter `invoices/`

Die generierten Dateien sind Arbeitsprodukte des Programms und werden nicht als Quellcode benötigt.

## Bewerbungsbezug

Als Bewerberprojekt zeigt dieses Repository, wie technische Messdaten in einen ERP-nahen Geschäftsprozess überführt werden können. Es verbindet Informatik, Energiewirtschaft, Datenanalyse und kaufmännisches Billing in einem nachvollziehbaren Python-Workflow.
