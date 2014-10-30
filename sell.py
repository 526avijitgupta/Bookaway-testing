# import pdb
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from local_settings import *


class BookawaySellTest(unittest.TestCase):

    def setUp(self):
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

    def test_sell_form_submission_bookaway(self):
        driver = self.driver
        driver.get("http://localhost/Books-for-bucks/sell.php")
        self.assertIn("Sell", driver.title)

        driver.maximize_window()
        
        my_dic = {'seller_name':None}
        input_list = []

        seller_names = open('input/seller_names.txt','r').readlines()
        seller_names = map(lambda each:each.strip('\n'),seller_names)

        seller_emails = open('input/seller_emails.txt','r').readlines()
        seller_emails = map(lambda each:each.strip('\n'),seller_emails)

        seller_phones = open('input/seller_phones.txt','r').readlines()
        seller_phones = map(lambda each:each.strip('\n'),seller_phones)

        seller_passwords = open('input/seller_passwords.txt','r').readlines()
        seller_passwords = map(lambda each:each.strip('\n'),seller_passwords)

        seller_colleges = open('input/seller_colleges.txt','r').readlines()
        seller_colleges = map(lambda each:each.strip('\n'),seller_colleges)

        seller_categories = open('input/seller_categories.txt','r').readlines()
        seller_categories = map(lambda each:each.strip('\n'),seller_categories)

        seller_books = open('input/seller_books.txt','r').readlines()
        seller_books = map(lambda each:each.strip('\n'),seller_books)



        #input_list = [
        #    'seller_name':seller_names
        #]

        # InputList is a list , with each index containing a dictionary , each dictionary having same components as each other , seller_name etc.

        for name in seller_names:
            #my_dic.update({'seller_name':name}) # Which is better
            my_dic['seller_name']=name
            input_list.append({'seller_name':name})
        # For input in input_list , input['seller_name']
        # pdb.set_trace() 
        for inp in input_list:
            name = driver.find_element_by_id("name")
            #name.send_keys("Avijit Gupta")
            name.send_keys(inp['seller_name'])
        
            email = driver.find_element_by_id("email")
            email.send_keys("526avijit@gmail.com")
        
            phone = driver.find_element_by_id("phone")
            phone.send_keys("9971958437")
        
            password = driver.find_element_by_id("password")
            password.send_keys("Avijit Gupta")
        
            sell_clg = driver.find_element_by_id("sell-clg")
            sell_clg.send_keys("JIIT Sector-62, Noida")
        
            # Make it better , this approach maybe wrong
            category = driver.find_element_by_id("subject")
            select_cat = [ cat for cat in category.find_elements_by_tag_name('option') if cat.text == 'Mathematics']
            select_cat[0].click()
        
            book = driver.find_element_by_id("book")
            book.send_keys("Puzzles to Puzzle You")
        
            author = driver.find_element_by_id("author")
            author.send_keys("Shakuntla Devi")
        
            s_cost = driver.find_element_by_id("s-cost")
            s_cost.send_keys("100")
        
            r_cost = driver.find_element_by_id("r-cost")
            r_cost.send_keys("100")
        
            driver.find_element_by_id("new-btn").click()
            # submit.send_keys(Keys.RETURN)

            driver.refresh()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
