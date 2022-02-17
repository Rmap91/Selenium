from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

BASE_URL = 'http://translate.google.com/'
driver = webdriver.Chrome()
driver.get(BASE_URL)
driver.find_element(by=By.XPATH, value="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys("i dont have hebrew on my VM")
sleep(1)
driver.find_element(by=By.XPATH, value="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button").click()
sleep(1)
driver.find_element(by=By.XPATH, value="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[2]/input").send_keys("hebrew")
sleep(1)
driver.find_element(by=By.XPATH, value="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[4]/div/div[1]/div[2]/span").click()

sleep(3)
driver.quit()




