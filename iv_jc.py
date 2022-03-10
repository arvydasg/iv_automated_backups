from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By # deprecation warning removed
from configparser import ConfigParser
from selenium import webdriver
import time


driver = webdriver.Chrome("/home/arvydas/Dropbox/src/iv_automated_backups/chromedriver")
driver.maximize_window()


def main():
    iv_login()
    do_backup()


def read_user():
    file = '/home/arvydas/Desktop/config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['jc']['user'])


def read_pass():
    file = '/home/arvydas/Desktop/config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['jc']['pass'])


def read_ivlt():
    file = '/home/arvydas/Desktop/config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['jc']['ivlt'])


def read_backup_page():
    file = '/home/arvydas/Desktop/config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['jc']['backup_page'])


def talpinimas():
    file = '/home/arvydas/Desktop/config.ini'
    config = ConfigParser()
    config.read(file)
    return(config['jc']['talpinimas'])


def iv_login():
    browser = driver.get(read_ivlt())
    driver.find_element(By.NAME, "nick").send_keys(read_user())
    driver.find_element(By.NAME, "password").send_keys(read_pass())
    time.sleep(10)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    print("logged_in")


def do_backup():
    browser = driver.get(talpinimas())
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "DirectAdmin").click()
    time.sleep(1)
    driver.get(read_backup_page())
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    print("backup JC done")

if __name__ == '__main__':
	main()
