import requests

url = "https://api.chucknorris.io/jokes/random"
result = requests.get(url)

print(result.text)
