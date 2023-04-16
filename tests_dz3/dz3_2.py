import requests
class TestDz3_2:

    def test_cookie(self):
        response = requests.post(
            "https://playground.learnqa.ru/api/homework_cookie"
        )
        print(response.cookies)

        assert response.cookies['HomeWork'] == 'hw_value', \
            f"Неправильный ответ cookie: {response.cookies['HomeWork']}"