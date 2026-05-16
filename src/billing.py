TARIFFS = {
    "HOUSEHOLD": {"base_fee": 12.0, "price_per_kwh": 0.32},
    "BUSINESS": {"base_fee": 39.0, "price_per_kwh": 0.28},
    "INDUSTRIAL": {"base_fee": 150.0, "price_per_kwh": 0.23},
}
TAX_RATE = 0.19


def calculate_bill(customer_type, kwh):
    tariff = TARIFFS[customer_type]
    net = tariff["base_fee"] + kwh * tariff["price_per_kwh"]
    tax = net * TAX_RATE
    return round(net + tax, 2)
