import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect', allow_redirects=True)

first_response = response.history[0]
sec_response = response.history[1]
ch_response = response.url

print(first_response.url)
print(sec_response.url)
print(ch_response)

