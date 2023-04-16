import requests

class TestDz3_3:

    def test_header_method(self):
        response = requests.post(
            "https://playground.learnqa.ru/api/homework_header"
        )
        print(response.headers)
        x_secret_hw_value = response.headers['x-secret-homework-header']
        excepted_result = "Секретное значение"

        assert x_secret_hw_value == excepted_result, \
            f"Некорректное 'x-secret-homework-header' значение в ответе. Актуальное значение: {x_secret_hw_value}"