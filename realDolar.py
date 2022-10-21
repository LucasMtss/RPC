import requests

req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

res = req.json()

print(res)