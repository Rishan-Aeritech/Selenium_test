import time; 
from Routes import *
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class LoginValidationTest(BaseCase):       
    def test_contructor(self):
        self.openPage()
        
    def openPage(self):
        self.baseUrl = LoginUrl
        self.open(self.baseUrl)
        self.assert_equal(self.get_current_url(),self.baseUrl,f"Failed to Open {self.baseUrl}")
        self._print(f"Login Page is opened successfully")
        # 
        self.fillBidderCredentials()
        # 
        self.click('button[type="submit"]')
        self.checkForValidationError()
        #
        time.sleep(2)
        
    def checkForValidationError(self):
        selector='[data-testid="validation-error"]'
        isExists = self.is_element_present(selector)
        if(isExists):
            message=f"Cannot Perform Login due to Validation Error on Fields: {self.get_text(selector)}"
            self._print(message)
        else:
            self._print("Empty Field was provided to check for validation error but no validation errors were encountered")
            self.fail(message)
        
    def loginWithCredentials(self,email,password):
        self.type('[name="email"]', email)
        self.type('[name="password"]',password)
        self._print(f"{email} and {password} is filled to input area")
        
    def fillBidderCredentials(self):
        self.loginWithCredentials("","")
        