import time; 
from Routes import *
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class LoginSuccessTest(BaseCase):       
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
        self.waitForApiCallToEnd()
        self.checkForApiResponseError()
        #
        time.sleep(2) #buffer time for page navigations
        self.assert_url(DashboardUrl)
        self._print("Navigated to Dashboard Page successfully")
        time.sleep(3)
        
            
    
    def waitForApiCallToEnd(self):
        loginSpinnnerSelector='[data-testid="login-loading"]'
        self.wait_for_element(loginSpinnnerSelector, timeout=5)
        self._print("Api call for login api has been started")
        self.wait_for_element_not_visible(loginSpinnnerSelector, timeout=5)
        self._print("Api call for login api has been ended")
        
    def checkForValidationError(self):
        selector='[data-testid="validation-error"]'
        isExists = self.is_element_present(selector)
        if(isExists):
            message=f"Cannot Perform Login due to Validation Error on Fields: {self.get_text(selector)}"
            self._print(message)
            self.fail(message)
            
    def checkForApiResponseError(self):
        selector='[data-testid="api-response-error"]'
        isExists = self.is_element_present(selector)
        if(isExists):
            message=f"Login Failed with message: {self.get_text(selector)}"
            self._print(message)
            self.fail(message)
        
    def loginWithCredentials(self,email,password):
        self.type('[name="email"]', email)
        self.type('[name="password"]',password)
        self._print(f"{email} and {password} is filled to input area")
        
    def fillBidderCredentials(self):
        self.loginWithCredentials("tech@aeritech.com","Test123$$")
        