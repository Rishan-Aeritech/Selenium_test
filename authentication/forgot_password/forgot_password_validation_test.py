import time; 
from authentication.forgot_password.forgot_password_navigation_test import  navigationTest
from constant.Routes import *
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class ForgotPasswordTest(BaseCase):       
    def test_swag_labs(self):
        self.openPage()
        
    def openPage(self):
        self.baseUrl = LoginUrl
        navigationTest(self)
        # 
        self.fillEmptyEmail()
        # 
        self.click('button[type="submit"]')
        self.checkForValidationError()
        # 
        time.sleep(4)
        
    def checkForValidationError(self):
        selector='[data-testid="validation-error"]'
        isExists = self.is_element_present(selector)
        if(isExists):
            message=f"Cannot Perform due to Validation Error on Fields: {self.get_text(selector)}"
            self._print(message)
        else:
            self.fail("Empty Email was provided but no validation error was occured")
        
    def addEmailToInputField(self,email):
        self.type('[name="email"]', email)
        self._print(f"{email} is filled to input area")
            
    
    def fillEmptyEmail(self):
        self.addEmailToInputField("")
        

        