import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import re
user_email = "" # enter your email address
user_pass = "" # enter your password
class FacebookAutomation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_facebook_automation_and_scrapping(self):
        driver = self.driver
        driver.get("https://www.facebook.com/") 
        
        self.assertIn("Facebook", driver.title)
        elem = driver.find_element_by_name("email")
        elem.clear()
        elem.send_keys(user_email)
        print "Email entered---->"
        
        elem1 = driver.find_element_by_name("pass")
        elem1.clear()
        elem1.send_keys(user_pass)
        print "Password entered---->"

        button = driver.find_element_by_id("loginbutton")
        button.click()
        print "Logged IN!"
        driver.implicitly_wait(20)


        #<---------For status update----------------->
        #<-----Post your status----------------------> 
        post_elem = driver.find_element_by_id("feedx_sprouts_container")
        driver.execute_script("arguments[0].scrollIntoView();", post_elem)
        webdriver.ActionChains(driver).move_to_element(post_elem).click(post_elem).perform()
        post_elem.click()
        print "Inside the Status Container"
        
        #post_click = driver.find_element_by_class_name("_45wg._69yt")
        #post_click.click()

        driver.implicitly_wait(10)

        #Scrapping Recent posts and Messages
        f = open ("inp.txt","w")
        soup = BeautifulSoup(driver.page_source,'html5lib')
        text = list()
        for link in soup.find_all('a'):
            f.write(str(link.get('href')).encode()+"\n")
           
        f.close()
        fobj = open("inp.txt")
        text = fobj.read()
        fobj.close()

        m = re.findall("https://www.facebook.com/messages/t/"+r'[0-9]+',text)
        print "---------------------------------------------------------------------------"
        print "Recent messages"
        print "---------------------------------------------------------------------------"
        print m
        print "---------------------------------------------------------------------------"
        
        container = soup.find('div', attrs = {'id':'stream_pagelet'})
        cont = {}
        i = 0
        for content in container.findAll('div', attrs = {'class': '_5pbx userContent _3ds9 _3576'}) + container.findAll('div', attrs = {'class': '_5pbx userContent _3576'}):
            driver.implicitly_wait(20)
            cont [i] = content.p.text
            i = i + 1
        print "---------------------------------------------------------------------------"
        print "Recent Posts (only TEXT)"
        print "---------------------------------------------------------------------------"

        for i in cont.items():
            print i

        assert "No results found." not in driver.page_source


if __name__ == "__main__":
    unittest.main()