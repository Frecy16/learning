import selenium
import time
from selenium import webdriver


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    time.sleep(3)
