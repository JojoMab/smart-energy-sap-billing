from src.billing import calculate_bill


def test_household_bill_includes_tax():
    assert calculate_bill("HOUSEHOLD", 100) == 52.36


def test_business_bill_is_positive():
    assert calculate_bill("BUSINESS", 500) > 0
