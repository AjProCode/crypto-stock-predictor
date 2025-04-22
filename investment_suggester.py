def suggest_investment(amount, risk='medium'):
    if risk == 'low':
        allocation = {'stocks': 0.3, 'crypto': 0.1, 'bonds': 0.6}
    elif risk == 'high':
        allocation = {'stocks': 0.5, 'crypto': 0.4, 'bonds': 0.1}
    else:
        allocation = {'stocks': 0.4, 'crypto': 0.3, 'bonds': 0.3}

    suggestion = {k: round(v * amount, 2) for k, v in allocation.items()}
    return suggestion