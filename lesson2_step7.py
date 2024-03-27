#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time



try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)

    first_name_input = browser.find_element(By.NAME, "firstname")
    first_name_input.send_keys("Gomid")

    last_name_input = browser.find_element(By.NAME, "lastname")
    last_name_input.send_keys("Gomigovi")

    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("Gomid@Gomigovi.com")


    # Получаем путь к домашней директории текущего пользователя
    home_dir = os.path.expanduser('~')
# Строим путь к папке "Downloads" в домашней директории
    downloads_path = os.path.join(home_dir, 'Downloads')
# Указываем путь к файлу 'example.txt', находящемуся в папке "Downloads"
    file_path = os.path.join(downloads_path, 'example.txt')




    #current_dir = os.path.abspath(os.path.dirname('Users/mac/Downloads'))    # получаем путь к директории текущего исполняемого файла 
    #file_path = os.path.join(current_dir, 'example.txt')           # добавляем к этому пути имя файла 
    
    file_input = browser.find_element(By.NAME, "file")
    file_input.send_keys(file_path)
    
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()  

