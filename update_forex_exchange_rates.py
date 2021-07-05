import requests
import numpy as np

# replace api_key with your own
api_key = 'bb192b23612a09196091fc69'
base_url = 'https://v6.exchangerate-api.com/v6/' + api_key

r = requests.get(base_url + '/codes')
currencies = np.array([currency[0] for currency in r.json()['supported_codes']])
np.save('forex_currencies.npy', currencies)

exchange_rate_matrix = []
for currency in currencies:
    r = requests.get(base_url + '/latest/' + currency)
    conversion_rates = list(r.json()['conversion_rates'].items())
    conversion_rates.sort()
    conversion_rates = [rate for cur, rate in conversion_rates]
    exchange_rate_matrix.append(conversion_rates)

exchange_rate_matrix = np.array(exchange_rate_matrix)
np.save('forex_exchange_rate_matrix.npy', exchange_rate_matrix)