from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

Base_URL = 'https://www.facebook.com/'

driver = webdriver.Chrome()
driver.get(Base_URL)
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("XXX")
sleep(1)
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys("XXX" + Keys.RETURN)

