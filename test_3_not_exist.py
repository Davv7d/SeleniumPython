#
# Checking if there is correct information when searching for an item that definitely does not exist
#
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestFindbook():
    def setup_method(self, method):
        self.driver = webdriver.Firefox(executable_path='geckodriver.exe')
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_item_not_exist(self):
        self.driver.get("https://www.olx.pl/")
        self.driver.set_window_size(1616, 876)
        time.sleep(1)
        self.driver.find_element(By.ID, "headerSearch").click()
        self.driver.find_element(By.ID, "headerSearch").send_keys(
            "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!@@@@@@@@@@@@@@@@@@@##############%%%%%%%%%%%%&^&&&&&&&&&&&&&&%((((((((()))))))))")
        time.sleep(1)
        self.driver.find_element(By.ID, "submit-searchmain").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "search-text").click()
        self.driver.find_element(By.ID, "search-text").send_keys(
            "!!@#!$!$!$@$@$!!$$$@#@#@#!$^(*)*()&*(&*(%GCVCXVcxvcxvcxvcxvssfdfsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsd")
        time.sleep(1)
        self.driver.find_element(By.ID, "search-submit").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".marker").text == "Sprawdź poprawność albo spróbuj bardziej ogólnego zapytania"
        self.driver.close()
