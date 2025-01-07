import time; 
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


# You'll notice that a logs folder, ./latest_logs/, was created to hold information (and screenshots) about the failing test. D
# uring test runs, past results get moved to the archived_logs folder 
# if you have ARCHIVE_EXISTING_LOGS set to True in settings.py, or 
# if your run tests with --archive-logs. If you choose not to archive existing logs, 
# they will be deleted and replaced by the logs of the latest test run.

# #abc->id
# .abc->class
# xyc[prop]->xyc represent html tag and inside[] represent properties of 'xyc' tag it should search for
class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.baseUrl = "https://www.facebook.com/"
        self.open(self.baseUrl)
        # time.sleep(3)  # Do nothing for 3 seconds.
        
        self.type('#email', "seth@equip-bid.com")
        
        self.type('#pass', "seth@equip-bid.com")

        time.sleep(2)
        
        # self.type('[name="email"]', "seth@equip-bid.com")
        # self.type('[name="password"]', "Test123$$")

        self.click('a[data-testid="open-registration-form-button"]')
        # self.click('button[type="submit"]')
        # self.click('button')

        # time.sleep(5) 
        # invalid email
        # self.type('[name="email"]', "seth")

        # self.assert_element('input:invalid')
        
        # self.click('a[href="/register"]')
        time.sleep(3) 
        self.currentUrl = self.get_current_url() 
        self.assert_equal(self.currentUrl, "https://www.facebook.com/r.php?entry_point=login","Pressed The Register button, but was not navigated there")
        # -> check the two values are equal or no
        # # time.sleep(2) 

        # self.wait_for_element_present("div.my_class", timeout=20)
        
        # self.click("#shopping_cart_container a")
        # self.assert_exact_text("Your Cart", "span.title")
        # self.assert_text("Backpack", "div.cart_item")
        # self.click("button#checkout")
        # self.type("#first-name", "SeleniumBase")
        # self.type("#last-name", "Automation")
        # self.type("#postal-code", "77123")
        # self.click("input#continue")
        # self.assert_text("Checkout: Overview")
        # self.assert_text("Backpack", "div.cart_item")
        # self.assert_text("29.99", "div.inventory_item_price")
        # self.click("button#finish")
        # self.assert_exact_text("Thank you for your order!", "h2")
        # self.assert_element('img[alt="Pony Express"]')
        # self.js_click("a#logout_sidebar_link")

        # self.assert_element("div#login_button_container")