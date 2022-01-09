from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By # deprecation warning removed
from configparser import ConfigParser

driver = webdriver.Chrome("/home/arvydas/Desktop/chromedriver")
driver.maximize_window()

def main():
    iv_login()

def iv_login():
    browser = driver.get("https://klientams.iv.lt/?command=signin")
    time.sleep(2)
    driver.find_element(By.NAME, "nick").send_keys(read_username())
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys(read_password())
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(2)

def read_username():

    file = 'config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['sf']['username'])

def read_password():

    file = 'config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['sf']['password'])

if __name__ == '__main__':
	main()

        
    # print(config.sections())
    # print(config['sf']) # object
    # print(list(config['sf'])) # list
    # print(config['sf']['username'])
