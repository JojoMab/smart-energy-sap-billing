import csv
from dataclasses import dataclass

from src.billing import calculate_bill
from src.energy_report import calculate_co2
from src.forecast import moving_average_forecast


@dataclass
class Reading:
    customer_type: str
    month: str
    kwh: float
    days: int


def monthly_cost(reading):
    """Compatibility helper for the original simple project tests."""
    return round(float(reading.kwh) * 0.31, 2)


def co2_kg(reading):
    """Compatibility helper for the original simple project tests."""
    return round(float(reading.kwh) * 0.38, 2)


def recommendation(reading):
    return "check efficiency potential" if float(reading.kwh) >= 800 else "normal usage"


def load_csv(path):
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def main():
    customers = {row["customer_id"]: row for row in load_csv("data/customer_data.csv")}
    consumption = load_csv("data/consumption_data.csv")
    print("ERP-nahe Billing-Simulation abgeschlossen.")
    for customer_id, customer in customers.items():
        values = [float(row["kwh"]) for row in consumption if row["customer_id"] == customer_id]
        latest_bill = calculate_bill(customer["customer_type"], values[-1])
        print(f"{customer['customer_name']}: letzte Rechnung {latest_bill:.2f} EUR, CO2 {calculate_co2(sum(values)):.2f} kg, Prognose {moving_average_forecast(values):.2f} kWh")


if __name__ == "__main__":
    main()
