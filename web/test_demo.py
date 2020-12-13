import time

from selenium import webdriver


class TestDemo:
    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_demo(self):
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("kw").send_keys("我要自学网")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]/em').is_displayed()
