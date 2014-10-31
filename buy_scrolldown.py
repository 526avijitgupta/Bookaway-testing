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
        current_scrollTop = 0
        new_scrollTop = int(driver.execute_script("return document.body.scrollHeight"))

        while (screen_height < new_scrollTop - current_scrollTop):
            driver.execute_script("window.scrollTo(0,"+str(new_scrollTop)+");")
            sleep(2)
            current_scrollTop = new_scrollTop
            new_scrollTop = int(driver.execute_script("return document.body.scrollHeight"))
        sleep(2)
            
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main()

    
