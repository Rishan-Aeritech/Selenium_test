from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class LoginTest(BaseCase):
    def test_swag_labs(self):
        self.open("https://admin-equip-bid-test.aeritech.com/login")
        self.type('input[name="password"]', "")
        self.click("div.col-lg-5 form button")
