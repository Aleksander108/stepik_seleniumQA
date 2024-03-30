#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import unittest

class Test_form_fill(unittest.TestCase):
    def test_form_fill1(self):
        
        # open the form page
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        # filler code for the required fields
        input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        input3.send_keys("oiojk@kljlk.cdj")
        
        # send the filled form
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # find the element concludig text
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # with assertEqual expected / real / 
        
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "huynya happened")
        
    def test_form_fill2(self):
        
        # open the form page
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        # filler code for the required fields
        input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        input3.send_keys("oiojk@kljlk.cdj")
        
        # send the filled form
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # find the element concludig text
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # with assertEqual expected / real / 
        
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "huynya happened")
      
    
if __name__ == "__main__":
    unittest.main()


# In[5]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




