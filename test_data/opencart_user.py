import random
import string


class RandomUserData:
    password = ""

    def random_string(self, lenght=10):
        return "".join([random.choice(string.ascii_letters) for _ in range(lenght)])

    def random_phone(self):
        return "".join([random.choice(string.digits) for _ in range(10)])

    def random_email(self):
        return self.random_string() + "@" + self.random_string(5) + "." + random.choice(["com", "ua", "org", "ru"])

    def random_password(self):
        self.password = "".join([random.choice(string.ascii_letters) for _ in range(5)])
        return self.password

    def password_confirm(self):
        return self.password
