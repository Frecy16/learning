from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_id("kw").send_keys("我要自学网")
driver.find_element_by_id("su").click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]/em').is_displayed()

time.sleep(8)
driver.quit()
