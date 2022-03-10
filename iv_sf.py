'''
Docstring idk?

idk.

'''


import time
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # deprecation warning removed


driver = webdriver.Chrome("/home/arvydas/Dropbox/src/iv_automated_backups/chromedriver")
driver.maximize_window()

'''
Docstring idk?

idk.

'''


def main():
    iv_login()
    do_backup()


def read_user():
    # read username from an external config file
    file = '/home/arvydas/Desktop/config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['sf']['user'])


def read_pass():
    # read password from an external config file
    file = '/home/arvydas/Desktop/config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['sf']['pass'])


def read_ivlt():
    # read website url from an external config file
    file = '/home/arvydas/Desktop/config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['sf']['ivlt'])


def read_backup_page():
    # read website url for a backup from an external config file
    file = '/home/arvydas/Desktop/config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['sf']['backup_page'])


def talpinimas():
    file = '/home/arvydas/Desktop/config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['sf']['talpinimas'])


def iv_login():
    # login to the website procedure
    # visit this site
    driver.get(read_ivlt())
    # find field by name "nick", enter configParser keys from function read_user
    driver.find_element(By.NAME, "nick").send_keys(read_user())
    # find field by name "password", enter configParser keys from function read_pass
    driver.find_element(By.NAME, "password").send_keys(read_pass())
    # sleep for me just in case it asks for a security code
    time.sleep(10)
    # find FIRST "submit" element and then click it
    driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()
    print("I'm in")


def do_backup():
    # procedure when logged in
    browser = driver.get(read_ivlt())
    time.sleep(1)
    # find element by link text - must match the text exactly
    driver.find_element(By.LINK_TEXT, "DirectAdmin").click()
    time.sleep(1)
    # go to another site - current one wouldn't let me click on "atsargines kopijos"
    driver.get(read_backup_page())
    time.sleep(1)
    # find FIRST "submit" element and then click it
    driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()
    time.sleep(1)
    print("backup SF done")


if __name__ == '__main__':
    main()
