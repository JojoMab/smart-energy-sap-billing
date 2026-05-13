
def calculate_bill(customer, analysis):
    energy_cost = analysis['grid_usage'] * customer['tariff']
    feed_in_credit = analysis['feed_in'] * customer['feed_in_tariff']
    net_amount = max(energy_cost - feed_in_credit, 0)

    return {
        'energy_cost': energy_cost,
        'feed_in_credit': feed_in_credit,
        'net_amount': net_amount
    }
