import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class BookawaySellTest(unittest.TestCase):

    def setUp(self):
        chromedriver = "/home/avijit/Downloads/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

    def test_sell_form_submission_bookaway(self):
        driver = self.driver
        driver.get("http://bookaway.in/sell")
        self.assertIn("Sell", driver.title)

        driver.maximize_window()

        name = driver.find_element_by_id("name")
        name.send_keys("Avijit Gupta")
        email = driver.find_element_by_id("email")
        email.send_keys("526avijit@gmail.com")
        phone = driver.find_element_by_id("phone")
        phone.send_keys("9971958437")
        password = driver.find_element_by_id("password")
        password.send_keys("Avijit Gupta")
        sell_clg = driver.find_element_by_id("sell-clg")
        sell_clg.send_keys("JIIT Sector-62, Noida")
        book = driver.find_element_by_id("book")
        book.send_keys("Puzzles to Puzzle You")
        author = driver.find_element_by_id("author")
        author.send_keys("Shakuntla Devi")
        
        sell_rent = Select(driver.find_element_by_id('sell-rent'))
        sell_rent.select_by_value("1")
        # select.select_by_index(index)
        # select.select_by_visible_text("text")

        s_cost = driver.find_element_by_id("s-cost")
        s_cost.send_keys("100")
        # r_cost = driver.find_element_by_id("r-cost")
        # r_cost.send_keys("100")
        submit = driver.find_element_by_id("new-btn")
        submit.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()