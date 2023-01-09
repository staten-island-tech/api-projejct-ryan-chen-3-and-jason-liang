import requests
import json

url = 'https://rest.coinapi.io/v1/assets'
headers = {'X-CoinAPI-Key' : '411BC328-3684-44CB-AC37-0200E00B2152'}
response = requests.get(url, headers=headers)
