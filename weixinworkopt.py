# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestWeiXinWorkOp:

    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)

    def teardown(self):
        self.driver.quit()

    def test_weixinworkbyoption(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']/span").click()
        time.sleep(3)




