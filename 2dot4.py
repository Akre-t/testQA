import requests
import json
import time

response1 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
parsed_response1 = response1.json()
print(parsed_response1['token'])
print(parsed_response1['seconds'])

payload = {"token": f"{parsed_response1['token']}"}
time.sleep(parsed_response1['seconds'])

response2 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload)

obj = json.loads(response2.text)

key = "status"

if key in obj:
    print(obj[key])
else:
    print(f"Задача еще не готова и объекта {key} еще нет")