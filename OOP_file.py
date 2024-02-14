from string import ascii_lowercase, digits
from typing import Any

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator
class LengthValidator:
    def __init__(self, min_length, max_length) -> None:
        self.min_lenght = min_length
        self.max_lenght = max_length
        
    def __call__(self, string) -> Any:
        lenght = len(string)
        return self.min_lenght <= lenght <= self.max_lenght


class CharsValidator:
    def __init__(self, chars) -> None:
        self.chars = chars
        
    def __call__(self, string):
        return all(char in self.chars for char in string)


lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")