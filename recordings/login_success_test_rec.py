from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class LoginSuccessTest(BaseCase):
    def test_contructor(self):
        self.open("https://admin-equip-bid-test.aeritech.com/login")
        self.type('input[name="email"]', "tech@aeritech.com")
        self.type('input[name="password"]', "Test123$$")
        self.click("div.col-lg-5 form button")
        self.wait_for_element('[data-testid="login-loading"]')
        self.assert_url("https://admin-equip-bid-test.aeritech.com/dashboard")
