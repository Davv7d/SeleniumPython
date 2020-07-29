#
# Logging in, check if it is possible to log in via fb, and try to log in with wrong data
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

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Firefox(executable_path='geckodriver.exe')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login_incorrect(self):
    self.driver.get("https://www.olx.pl/")
    self.driver.set_window_size(1616, 876)
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".link:nth-child(2) > strong").click()
    time.sleep(1)
    elements = self.driver.find_elements(By.ID, "fblogin")
    assert len(elements) > 0
    time.sleep(1)
    self.driver.find_element(By.ID, "userEmail").click()
    self.driver.find_element(By.ID, "userEmail").send_keys("xxxxxx@x.x")
    self.driver.find_element(By.ID, "userPass").send_keys("xxxxxxxxxxx")
    self.driver.find_element(By.ID, "se_userLogin").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, ".error:nth-child(1)").text == "nieprawidłowy login lub hasło"
    self.driver.close()

  def test_password_reminder(self):
    self.driver.get("https://www.olx.pl/")
    self.driver.set_window_size(1616, 876)
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "#postNewAdLink > span").click()
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Przypomnienie hasła").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".login-box__title").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, ".login-box__title").text == "Zapomniałeś hasła?"
    self.driver.find_element(By.CSS_SELECTOR, ".login-box__paragraph").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("abc@wp.pl")
    self.driver.find_element(By.ID, "se_userSignIn").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".login-box__title").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, ".login-box__title").text == "Wpisz kod i nowe hasło"
    self.driver.close()
if __name__ == '__main__':
  pytest.main()
