import os
import time
from time import sleep
from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.common.by import By
from utils.browser import make_chrome_browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class FunctionalTestsProducts(TestCase, StaticLiveServerTestCase):
    
    #test functional food pages
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_food_list_page_create_page_and_detail_page(self):
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        browser.maximize_window()
        wait = WebDriverWait(browser, 10)
        sleep(1)
        log = browser.find_element(By.ID, 'log')
        log.click()
        sleep(2)
        register = browser.find_element(By.ID, 'register')
        register.click()
        username = browser.find_element(By.NAME, "username")
        username.send_keys("TesteSelenium2")
        sleep(1)
        email = browser.find_element(By.NAME, "email")
        email.send_keys("Sselenium2@gmail.com")
        sleep(2)
        typeUser = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@class="form-control select"]')))
        select = Select(typeUser)
        select.select_by_value('fooddivider')
        sleep(1)
        password1 = browser.find_element(By.NAME, "password1")
        password1.send_keys("sel12345.")
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("sel12345.")
        password2.send_keys(Keys.RETURN)
        sleep(2)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("Sselenium2@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sel12345.")
        password.send_keys(Keys.RETURN)
        sleep(2)
        hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
        hbg.click()
        sleep(2)
        alm = wait.until(EC.presence_of_element_located((By.ID, 'alimentos')))
        alm.click()
        sleep(2)
        alm1 = wait.until(EC.presence_of_element_located((By.ID, 'alimentos2')))
        alm1.click()
        sleep(2)
        FoodCreate = wait.until(EC.presence_of_element_located((By.ID, "create_food")))
        FoodCreate.click()
        sleep(2)
        name = browser.find_element(By.NAME, "name")
        name.send_keys("Arroz Branco")
        sleep(1)
        qtdd = browser.find_element(By.NAME, "quantity")
        qtdd.send_keys(4)
        sleep(1)
        date = browser.find_element(By.NAME, "validity")
        date.send_keys("01/03/2023")
        sleep(4)
        category = browser.find_element(By.NAME, "typeCategoria")
        select = Select(category)
        select.select_by_visible_text("INOMPNP")
        sleep(2)
        btnCreate = wait.until(EC.presence_of_element_located((By.ID, "btn_enviar")))
        browser.execute_script("arguments[0].click();", btnCreate)
        sleep(5)
        food_detail = wait.until(EC.presence_of_element_located((By.ID, "food_detail")))
        browser.execute_script("arguments[0].click();", food_detail)
        sleep(3)
        quantity = browser.find_element(By.NAME, "quantity")
        quantity.send_keys(3)
        sleep(1)
        submit = wait.until(EC.presence_of_element_located((By.ID, 'btn-submit')))
        browser.execute_script("arguments[0].click();", submit)
        assert "Detail Food" in browser.title
        sleep(3)
        browser.quit()
        
    def test_request_food_and_list_page(self):
        
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        browser.maximize_window()
        wait = WebDriverWait(browser, 10)
        sleep(1)
        log = browser.find_element(By.ID, 'log')
        log.click()
        sleep(1)
        register = browser.find_element(By.ID, 'register')
        register.click()
        username = browser.find_element(By.NAME, "username")
        username.send_keys("TesteSelenium2")
        sleep(1)
        email = browser.find_element(By.NAME, "email")
        email.send_keys("Sselenium2@gmail.com")
        sleep(2)
        typeUser = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@class="form-control select"]')))
        select = Select(typeUser)
        select.select_by_value('secretary')
        sleep(1)
        password1 = browser.find_element(By.NAME, "password1")
        password1.send_keys("sel12345.")
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("sel12345.")
        password2.send_keys(Keys.RETURN)
        sleep(2)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("Sselenium2@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sel12345.")
        password.send_keys(Keys.RETURN)
        sleep(2)
        hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
        hbg.click()
        sleep(5)
        alm = wait.until(EC.presence_of_element_located((By.ID, 'alimentos')))
        alm.click()
        sleep(5)
        alm1 = wait.until(EC.presence_of_element_located((By.ID, 'alimentos3')))
        alm1.click()
        ReqFood = wait.until(EC.presence_of_element_located((By.ID, 'req_food')))
        ReqFood.click()
        input = browser.find_element(By.NAME, "name")
        input.send_keys("Feijão")
        BtnRequest = wait.until(EC.presence_of_element_located((By.ID, 'btnRequest')))
        BtnRequest.click()
        assert "List Food" in browser.title
        sleep(1)
        browser.quit()
        
        
    #test functional cleaning pages
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_cleaning_list_page_request_cleaning_and_detail_cleaning(self):
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        browser.maximize_window()
        wait = WebDriverWait(browser, 10)
        sleep(1)
        log = browser.find_element(By.ID, 'log')
        log.click()
        sleep(1)
        register = browser.find_element(By.ID, 'register')
        register.click()
        username = browser.find_element(By.NAME, "username")
        username.send_keys("TesteSelenium2")
        sleep(1)
        email = browser.find_element(By.NAME, "email")
        email.send_keys("Sselenium2@gmail.com")
        sleep(2)
        typeUser = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@class="form-control select"]')))
        select = Select(typeUser)
        select.select_by_value('fooddivider')
        sleep(1)
        password1 = browser.find_element(By.NAME, "password1")
        password1.send_keys("sel12345.")
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("sel12345.")
        password2.send_keys(Keys.RETURN)
        sleep(2)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("Sselenium2@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sel12345.")
        password.send_keys(Keys.RETURN)
        sleep(2)
        hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
        hbg.click()
        sleep(2)
        alm = wait.until(EC.presence_of_element_located((By.ID, 'limpeza')))
        alm.click()
        sleep(2)
        alm1 = wait.until(EC.presence_of_element_located((By.ID, 'limpeza1')))
        alm1.click()
        add_cleaning = wait.until(EC.presence_of_element_located((By.ID, 'add_cleaning')))
        add_cleaning.click()
        input = browser.find_element(By.NAME, "name")
        input.send_keys("Desinfetante")
        input2 = browser.find_element(By.NAME, "quantity")
        input2.send_keys(10)
        BtnRequest = wait.until(EC.presence_of_element_located((By.ID, 'btn_cleaning')))
        BtnRequest.click()
        DTcleaning = browser.find_element(By.ID, "detail_cleaning")
        DTcleaning.click()
        newQTDD = browser.find_element(By.NAME, "quantity")
        newQTDD.send_keys(4)
        btnSubmit = browser.find_element(By.ID, "btnSubmit")
        btnSubmit.click()
        assert "Detail Cleaning" in browser.title
        sleep(1)
        browser.quit()
        
    def test_request_cleaning_page(self):  
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        browser.maximize_window()
        wait = WebDriverWait(browser, 10)
        sleep(1)
        log = browser.find_element(By.ID, 'log')
        log.click()
        sleep(1)
        register = browser.find_element(By.ID, 'register')
        register.click()
        username = browser.find_element(By.NAME, "username")
        username.send_keys("TesteSelenium2")
        sleep(1)
        email = browser.find_element(By.NAME, "email")
        email.send_keys("Sselenium2@gmail.com")
        sleep(2)
        typeUser = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@class="form-control select"]')))
        select = Select(typeUser)
        select.select_by_value('asg')
        sleep(1)
        password1 = browser.find_element(By.NAME, "password1")
        password1.send_keys("sel12345.")
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("sel12345.")
        password2.send_keys(Keys.RETURN)
        sleep(2)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("Sselenium2@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sel12345.")
        password.send_keys(Keys.RETURN)
        sleep(2)
        hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
        hbg.click()
        sleep(2)
        alm = wait.until(EC.presence_of_element_located((By.ID, 'limpeza')))
        alm.click()
        sleep(2)
        alm1 = wait.until(EC.presence_of_element_located((By.ID, 'limpeza2')))
        alm1.click()
        RQTcleaning = browser.find_element(By.ID, "request_cleaning")
        RQTcleaning.click()
        input = browser.find_element(By.NAME, "name")
        input.send_keys('Desinfetante')
        btnRQTcleaning = browser.find_element(By.ID, "btnRQTcleaning")
        btnRQTcleaning.click()
        assert "List request" in browser.title
        sleep(1)
        browser.quit()
