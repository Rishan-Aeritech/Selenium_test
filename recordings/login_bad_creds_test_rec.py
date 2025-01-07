from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class LoginBadCredsTest(BaseCase):
    def test_contructor(self):
        self.open("https://admin-equip-bid-test.aeritech.com/login")
        self.type('input[name="email"]', "one@aeritech.com")
        self.type('input[name="password"]', "Test")
        self.click("div.col-lg-5 form button")
        self.wait_for_element('[data-testid="login-loading"]')
