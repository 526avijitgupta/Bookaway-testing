import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

from local_settings import *

class BookawayBuyTest(unittest.TestCase):

    def setUp(self):
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

    def test_sell_form_submission_bookaway(self):
        driver = self.driver
        driver.get("http://localhost/Books-for-bucks/buy.php")
        self.assertIn("Buy", driver.title)

        driver.maximize_window()
        screen_height = int(driver.execute_script("return window.screen.height"))
        current_scrollTop = int(driver.execute_script("return document.body.scrollHeight"))
        page_height = int(driver.execute_script("return document.body.scrollHeight"))
        new_scrollTop = 0
        while (current_scrollTop - new_scrollTop > screen_height ):
            new_scrollTop = current_scrollTop
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            driver.execute_script("window.scrollTo(0, "+str(page_height)+");")
            new_scrollTop = int(driver.execute_script("return document.body.scrollTop"))
            page_height = int(driver.execute_script("return document.body.scrollHeight"))
            print new_scrollTop,"new_scrollTop"
            print page_height,"page_height"
            print current_scrollTop,"current_scrollTop"
            print screen_height,"screen_height"
        


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main()

    
