
from selenium import webdriver
from time import sleep
BASE_URL1 = 'http://www.walla.co.il/'
BASE_URL2 = 'http://www.ynet.co.il'
def chrome():
    driver = webdriver.Chrome()
    #driver.get(BASE_URL1)
    #driver.get(BASE_URL2)
    sleep(2)
    name = driver.title
    print(f"this is from chrome: ",name)
    driver.quit()

def firefox():
    driver = webdriver.Firefox()
    driver.get(BASE_URL2)
    sleep(2)
    name = driver.title
    print(f"this is from firefox: ",name)
    driver.quit()

chrome()
firefox()



