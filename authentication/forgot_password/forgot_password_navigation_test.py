import time; 
from constant.Routes import *
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class ForgotPassswordNavigationTest(BaseCase):       
    def test_swag_labs(self):
        self.openPage()
        
    def openPage(self):
        navigationTest(self)
        
    
            
def navigationTest(obj):
    obj.baseUrl = LoginUrl
    obj.open(obj.baseUrl)
    obj.assert_equal(obj.get_current_url(),obj.baseUrl,f"Failed to Open {obj.baseUrl}")
    obj._print(f"Login Page is opened successfully")
    # 
    selector='[data-testid="forgot-password-ref"]'
    obj.click(selector)
    time.sleep(2) #buffer time for page navigations
    obj.assert_url(ForgotPasswordUrl)
    obj._print("Navigated to Forgot Password Page successfully")
    time.sleep(3) 