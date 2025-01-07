from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class ForgotPassswordNavigationTest(BaseCase):
    def test_swag1_labs(self):
        self.open("https://admin-equip-bid-test.aeritech.com/login")
        self.click('a[data-testid="forgot-password-ref"]')
        self.assert_url("https://admin-equip-bid-test.aeritech.com/forgot-password")
