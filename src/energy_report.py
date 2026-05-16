CO2_FACTOR_KG_PER_KWH = 0.233


def calculate_co2(kwh):
    return round(kwh * CO2_FACTOR_KG_PER_KWH, 2)


def summarize_consumption(consumption_rows):
    total_kwh = sum(float(row["kwh"]) for row in consumption_rows)
    return {
        "total_kwh": round(total_kwh, 2),
        "co2_kg": calculate_co2(total_kwh),
    }
