import sys
import os

# Add the parent folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'constant')))

import time; 
from Routes import *
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class ForgotPassswordNavigationTest(BaseCase):       
    def test_contructor(self):
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