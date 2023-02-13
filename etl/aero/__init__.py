import requests as r


url = 'http://18.179.144.185:8000/api/v1/auth/login?self=self'
data = {
  "username": "'yUtZQv6Lqa17F82tINWF2S7JqG_nrVfseqoGYXkbO_I='",
  "password": "'K1Yfdd47ybxap4xEIxAOSG4MQ5F6W716YqP3Tjz75sU='"
}
header = {'accept': 'application/json', 'Content-Type': 'application/json'}

response = r.post(url=url, json=data, headers=header)
access_token = response.json()['access_token']


url = 'http://18.179.144.185:8000/api/v1/c3/new_account_limit_orders?self=self'
data = {
  "exchange_name": "binance_usdt_m",
  "instrument_name": "ETHUSDT",
  "label_name": "BINANCE_IA"
}
header = {'accept': 'application/json', 'Content-Type': 'application/json', 'authorization': access_token}

response = r.post(url=url, json=data, headers=header)
print(response.status_code)
print(response.json())