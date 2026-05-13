from collections import defaultdict


def analyze_customer_energy(records, peak_threshold=2.0):
    total_consumption = sum(r['consumption'] for r in records)
    total_production = sum(r['production'] for r in records)
    grid_usage = sum(max(r['consumption'] - r['production'], 0) for r in records)
    feed_in = sum(max(r['production'] - r['consumption'], 0) for r in records)
    peaks = [r for r in records if r['consumption'] >= peak_threshold]

    monthly = defaultdict(lambda: {'consumption': 0.0, 'production': 0.0})
    for r in records:
        month = r['timestamp'].strftime('%Y-%m')
        monthly[month]['consumption'] += r['consumption']
        monthly[month]['production'] += r['production']

    avg_hourly = total_consumption / len(records) if records else 0
    forecast_month = avg_hourly * 24 * 30

    return {
        'total_consumption': total_consumption,
        'total_production': total_production,
        'grid_usage': grid_usage,
        'feed_in': feed_in,
        'peaks': peaks,
        'monthly': dict(monthly),
        'forecast_month': forecast_month
    }
