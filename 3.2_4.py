from string import ascii_lowercase, digits


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


class LengthValidator:
    def __init__(self, min, max):
        self.min_lenght = min
        self.max_lenght = max

    def __call__(self, *args, **kwargs):
        if self.min_lenght <= len(args[0]) <= self.max_lenght:
            return True


class CharsValidator:
    def __init__(self, string):
        self.string = string

    def __call__(self, *args, **kwargs):
        temp_lst = []
        for x in range(self.string):
            if self.string[x] in args[0]:
                temp_lst.append(self.string[x])
        if len("".join(temp_lst)) == len(self.string):
            return True


lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")
