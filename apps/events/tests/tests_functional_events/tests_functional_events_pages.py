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

class FunctionalTestsEvents(TestCase, StaticLiveServerTestCase):
    
    def test_events_list_page_create_event_page_and_detail_event(self):
        
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
        sleep(1)
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("sel12345.")
        password2.send_keys(Keys.RETURN)
        sleep(2)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("Sselenium2@gmail.com")
        sleep(1)
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sel12345.")
        password.send_keys(Keys.RETURN)
        sleep(2)
        hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
        hbg.click()
        sleep(2)
        events = browser.find_element(By.ID, "eventos")
        events.click()
        sleep(1)
        addEvent = browser.find_element(By.ID, "btn_addEvent")
        addEvent.click()
        sleep(1)
        nameEvent = browser.find_element(By.NAME, "name")
        nameEvent.send_keys('Formatura')
        sleep(1)
        dateEvent = browser.find_element(By.NAME, "date")
        dateEvent.send_keys('23/03/2023')
        sleep(1)
        school = browser.find_element(By.NAME, "school")
        select2 = Select(school)
        select2.select_by_visible_text("Maria Dália")
        sleep(1)
        btnCreate = browser.find_element(By.ID, "btn_event_create")
        btnCreate.click()
        sleep(1)
        btn_detail_event = browser.find_element(By.ID, "btn_detail_event")
        browser.execute_script("arguments[0].click();", btn_detail_event)
        sleep(1)
        hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
        hbg.click()
        sleep(2)
        events2 = browser.find_element(By.ID, "eventos")
        events2.click()
        sleep(1)
        edit = browser.find_element(By.ID, "btn_edit_event")
        browser.execute_script("arguments[0].click()", edit)
        sleep(2)
        nameEvent2 = browser.find_element(By.NAME, "name")
        nameEvent2.send_keys('Formatura')
        sleep(1)
        dateEvent2 = browser.find_element(By.NAME, "date")
        dateEvent2.send_keys('23/03/2023')
        sleep(1)
        school2 = browser.find_element(By.NAME, "school")
        select3 = Select(school2)
        select3.select_by_visible_text("Maria Dália")
        sleep(1)
        btnCreate2 = browser.find_element(By.ID, "btn_event_create")
        btnCreate2.click()
        sleep(1)
        delete = browser.find_element(By.ID, "btn_delete_event")
        browser.execute_script("arguments[0].click()", delete)
        sleep(2)
        btnDelete = browser.find_element(By.ID, "cancel_delete")
        browser.execute_script("arguments[0].click()", btnDelete)
        assert "List Events" in browser.title
        sleep(3)
        browser.quit()