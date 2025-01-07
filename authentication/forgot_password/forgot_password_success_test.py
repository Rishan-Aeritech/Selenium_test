
import time; 
from forgot_password_navigation_test import  navigationTest
from Routes import *
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class ForgotPasswordSuccessTest(BaseCase):       
    def test_contructor(self):
        self.openPage()
        
    def openPage(self):
        self.baseUrl = LoginUrl
        navigationTest(self)
        # 
        self.fillValidEmail()
        # 
        self.click('button[type="submit"]')
        self.checkForValidationError()
        # 
        self.waitForApiCallToEnd()
        self.checkForApiResponse()
        #
        time.sleep(4)
        
            
    
    def waitForApiCallToEnd(self):
        loginSpinnnerSelector='[data-testid="submit-loading"]'
        self.wait_for_element(loginSpinnnerSelector, timeout=5)
        self._print("Api call to request password reset has been started")
        self.wait_for_element_not_visible(loginSpinnnerSelector, timeout=5)
        self._print("Api call to request password reset has been ended")
        
    def checkForValidationError(self):
        selector='[data-testid="validation-error"]'
        isExists = self.is_element_present(selector)
        if(isExists):
            message=f"Cannot Perform due to Validation Error on Fields: {self.get_text(selector)}"
            self._print(message)
            self.fail(message)
            
    def checkForApiResponse(self):
        selector='.Toastify__toast--error'
        isExists = self.is_element_present(selector)
        if(isExists):
            message=f"Password Reset Request Failed with message: {self.get_text(selector)}"
            self._print(message)
            self.fail(message)
        
        selector='.Toastify__toast--success'
        isExists = self.is_element_present(selector)
        if(isExists):
            message=f"Password Reset Request Success with message: {self.get_text(selector)}"
            self._print(message)
        else:
            self._print(message)
            self.fail(message)
            
        
    def addEmailToInputField(self,email):
        self.type('[name="email"]', email)
        self._print(f"{email} is filled to input area")
            
    def fillValidEmail(self):
        self.addEmailToInputField("tech@aeritech.com")

        