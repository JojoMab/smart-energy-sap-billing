# Smart Energy SAP Billing System

Smart Energy SAP Billing System is a Python project that analyzes smart meter data and automatically creates energy reports and customer invoices. The workflow is intentionally close to SAP and ERP processes: measurement data is imported, evaluated from a business perspective and transformed into billable documents.

## GitHub Description

Python project for smart meter analysis and SAP-like energy billing with automated reports and invoices.

## Recruiter Snapshot

- Topic: energy industry, smart metering, billing and ERP-like processes
- Technology: Python, CSV processing, modular project structure
- Input: customer data and smart meter readings
- Output: energy reports and invoices per customer
- Focus: connection between technical data analysis and commercial billing

## Practical Workflow

The project simulates a digital process from the energy industry:

1. Smart meters provide measurement data.
2. The system reads customer and meter data from CSV files.
3. Consumption, production, grid usage and feed-in are calculated.
4. An energy report is created for each customer.
5. The analysis values are transformed into an invoice with feed-in credit.

## Features

- read customer data
- read smart meter data
- calculate consumption and production
- evaluate grid usage and feed-in
- detect peak loads
- create a monthly balance
- derive a consumption forecast
- generate invoices with feed-in credit

## Quick Start

Run the project from the repository root:

```bash
python3 main.py
```

Expected terminal output:

```txt
Report created: reports/smart_meter_report_C001.txt
Invoice created: invoices/invoice_C001_2026-05-15.txt
----------------------------------------
Report created: reports/smart_meter_report_C002.txt
Invoice created: invoices/invoice_C002_2026-05-15.txt
----------------------------------------
Report created: reports/smart_meter_report_C003.txt
Invoice created: invoices/invoice_C003_2026-05-15.txt
----------------------------------------
Report created: reports/smart_meter_report_C004.txt
Invoice created: invoices/invoice_C004_2026-05-15.txt
----------------------------------------
Report created: reports/smart_meter_report_C005.txt
Invoice created: invoices/invoice_C005_2026-05-15.txt
----------------------------------------
```

## Examples

The example outputs are versioned intentionally so recruiters can inspect the result directly on GitHub without running the project locally:

- [Terminal output](examples/terminal_output.txt)

The terminal output shows which reports and invoices are generated for the sample customers.

## Project Structure

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

## Input Data

`data/customers.csv` contains customer information such as tariff, name and customer ID. `data/meter_data.csv` contains the meter readings per customer, including consumption, production and timestamp.

## Outputs

Running the program creates for each customer:

- an energy report under `reports/`
- an invoice under `invoices/`

The generated files are working outputs of the program and are not required as source code.

## Portfolio Relevance

This project shows how technical measurement data can be transformed into an ERP-like business process. It connects computer science, energy industry logic, data analysis and commercial billing in a traceable Python workflow.
