import random


class TestLogin:
    def test_login1(self):
        print("test_login1")

    def test_login2(self):
        num = random.randint(0, 2)
        assert not num

    def test_login3(self):
        print("test_login123")
