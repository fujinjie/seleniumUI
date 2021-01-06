# -*- coding: utf-8 -*-
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

class TestWeiXinWorkCo:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_store_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(15)
        cookies = self.driver.get_cookies()
        with open("cookies.txt","w") as f:
            json.dump(cookies, f)

    def test_weixinworkbycookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        with open("cookies.txt","r") as f:
            cookies = json.load(f)
            for cookie in cookies:
                if "expiry" in cookie.keys():
                    cookie.pop("expiry")
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(2)
        self.driver.refresh()
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']/span").click()
        time.sleep(3)

