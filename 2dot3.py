import requests

# response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
# print(response.text)

# response = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type', data='HEAD')
# print(response.status_code)
#
# response = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type')
# print(response.status_code)

# response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params='PUT')
# print(response.text)

for_get = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]
for param in for_get:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
    print(f"Текст ответа: {response.text}, статус ответа: {response.status_code}, переданный параметр: {param}")

    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
    print(f"Текст ответа: {response.text}, статус ответа: {response.status_code}, переданный параметр: {param}")

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
    print(f"Текст ответа: {response.text}, статус ответа: {response.status_code}, переданный параметр: {param}")

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
    print(f"Текст ответа: {response.text}, статус ответа: {response.status_code}, переданный параметр: {param}")

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
    print(f"Текст ответа: {response.text}, статус ответа: {response.status_code}, переданный параметр: {param}")

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
    print(f"Текст ответа: {response.text}, статус ответа: {response.status_code}, переданный параметр: {param}")

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
    print(f"Текст ответа: {response.text}, статус ответа: {response.status_code}, переданный параметр: {param}")

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
    print(f"Текст ответа: {response.text}, статус ответа: {response.status_code}, переданный параметр: {param}")


