from src.energy_report import calculate_co2
from src.forecast import moving_average_forecast


def test_co2_calculation():
    assert calculate_co2(1000) == 233.0


def test_moving_average_forecast_uses_last_three_values():
    assert moving_average_forecast([100, 200, 300, 600]) == 366.67
