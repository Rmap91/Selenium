from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
BASE_URL = 'https://www.youtube.com/'
driver = webdriver.Chrome()
driver.get(BASE_URL)
sleep(1)
driver.find_element(by=By.XPATH, value="/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").click()
driver.find_element(by=By.XPATH, value="/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("Hello World" + Keys.ENTER)
