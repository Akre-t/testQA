import requests
import pytest

class TestUserAuth:
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "Здесь нет куки"
        assert "x-csrf-token" in response1.headers, "Здесь нет токена в заголовках"
        assert "user_id" in response1.json(), "Здесь нет ИД юзера"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x_csrf_token")
        self.user_id_from_auth_method = response1.json()["user_id"]
    def test_auth_user(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token":self.token},
            cookies={"auth_sid":self.auth_sid},
        )

        assert "user_id" in response2.json(), "Во втором запросе нет ИД юзера "
        user_id_from_check_method = response2.json()["user_id"]

        assert self.user_id_from_auth_method == user_id_from_check_method, "ИД юзера из метода авторизации не совпадает с ИД юзера из метода проверки"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):

        if condition == "no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers= {"x_csrf_token" : self.token}
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies= {"auth_sid" : self.auth_sid}
            )

        assert "user_id" in response2.json(), "Здесь нет ИД юзера во втором запросе"

        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_check_method == 0, f"Пользователь авторизован со следующими параметрами {condition}"