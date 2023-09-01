import json


class Checking:
    """Методы для проверки ответов запросов"""

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, print("Провал!!!")
        print(f"Успешно!!! Статус код = {result.status_code}")

    @staticmethod
    def check_json_token(result, expected_value):
        """Метод для проверки наличия обязательных полей в теле запроса"""
        token = json.loads(result.text)
        assert list(token) == expected_value
        print('Все поля присутствуют')

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        """Метод для проверки значения обязательных полей в теле запроса"""
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'{field_name} верен!!!')
