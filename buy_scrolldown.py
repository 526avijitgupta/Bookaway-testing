import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from local_settings import *

class BookawayBuyTest(unittest.TestCase):

    def setUp(self):
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

    def test_sell_form_submission_bookaway(self):
        driver = self.driver
        driver.get("http://bookaway.in/buy")
        self.assertIn("Buy", driver.title)

        driver.maximize_window()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main()

    
