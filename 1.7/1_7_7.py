class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])

class  TextInput:

        CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + 'qwertyuiopasdfghjklzxcvbnm'
        CHARS_CORRECT = CHARS + CHARS.upper() + '1234567890' + ' '

        def __init__(self, name, size=10):
            self.name = name
            self.size = size
            self.check_name(self.name)

        def get_html(self):
            return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

        @classmethod
        def check_name(cls, name):
            try:
                assert 3 <= len(name) <= 50 and all(c in cls.CHARS_CORRECT for c in name)
            except AssertionError:    
                raise ValueError("некорректное поле name")
            

class PasswordInput:

        CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + 'qwertyuiopasdfghjklzxcvbnm'
        CHARS_CORRECT = CHARS + CHARS.upper() + '1234567890' + ' '

        def __init__(self, name, size=10):
            self.name = name
            self.size = size
            self.check_name(self.name)

        def get_html(self):
            return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

        @classmethod
        def check_name(cls, name):
            try:
                assert 3 <= len(name) <= 50 and all(c in cls.CHARS_CORRECT for c in name)
            except AssertionError:    
                raise ValueError("некорректное поле name")


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()