def moving_average_forecast(values, window=3):
    if not values:
        return 0
    selected = values[-window:]
    return round(sum(selected) / len(selected), 2)
