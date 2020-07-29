#
# Checking whether when searching for 2 different elements, we correctly separate the elements on the page into highlighted and other elements
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
  
  def test_findBook(self):
    self.driver.get("https://www.olx.pl/")
    self.driver.set_window_size(1616, 876)
    time.sleep(1)
    self.driver.find_element(By.ID, "headerSearch").send_keys("programowanie w python")
    self.driver.find_element(By.ID, "headerSearch").send_keys(Keys.ENTER)
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) h2").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) h2").text == "Wyróżnione ogłoszenia\nZobacz wszystkie"
    self.driver.find_element(By.ID, "searchbox").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".hasPromoted > h2").text == "Pozostałe ogłoszenia"
    self.driver.close()

  def test_findBall(self):
    self.driver.get("https://www.olx.pl/")
    self.driver.set_window_size(1616, 876)
    time.sleep(1)
    self.driver.find_element(By.ID, "headerSearch").click()
    time.sleep(1)
    self.driver.find_element(By.ID, "headerSearch").send_keys("piłka nożna")
    self.driver.find_element(By.ID, "headerSearch").send_keys(Keys.ENTER)
    time.sleep(1)
    self.driver.find_element(By.ID, "paramsList").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, ".paramsList__title").text == "Filtry"
    assert self.driver.find_element(By.CSS_SELECTOR, ".paramsList__title").text == "Filtry"
    assert self.driver.find_element(By.CSS_SELECTOR, ".paramsList__title").text == "Filtry"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".paramsList__title")
    assert len(elements) > 0
    self.driver.close()
  
