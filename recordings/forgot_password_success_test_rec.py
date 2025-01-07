from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class ForgotPasswordSuccessTest(BaseCase):
    def test_contructor(self):
        self.open("https://admin-equip-bid-test.aeritech.com/login")
        self.click('a[data-testid="forgot-password-ref"]')
        self.assert_url("https://admin-equip-bid-test.aeritech.com/forgot-password")
        self.type('input[name="email"]', "tech@aeritech.com")
        self.click('button:contains("Request Password Reset")')
        self.wait_for_element('[data-testid="submit-loading"]')
