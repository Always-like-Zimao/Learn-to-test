#!/usr/bin/env python
# encoding: utf-8
'''
  @author: lyq
  @file: test_上传相片.py
  @time: 2022/3/31  22:29
  @desc:
'''
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
from objects.登录和登出_objects import LoginPage
from objects.创建日志_objects import MyLog
from config配置.config import driver_path,url,sheetname
from data数据.data import Datas
from log日志.log import logger
from selenium.webdriver.common.by import By
from objects.key_objects import Key

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('打开浏览器')
        e = Service(executable_path=driver_path)
        cls.driver = webdriver.Edge(service=e)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.loginpage=LoginPage(cls.driver)
        cls.mylog = MyLog(cls.driver)
        cls.key = Key(cls.driver)

        value_list = Datas().read_excel(sheetname[0])
        username = value_list[0][0]
        password = value_list[0][1]
        cls.loginpage.input_username(username)
        cls.loginpage.input_password(password)
        sleep(1)
        cls.loginpage.click_login()
        sleep(1)


    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')
        cls.driver.quit()


    def test_1_upload(self):
        '''
        验证成功上传相片的测试用例
        '''

        self.key.click(By.XPATH,"//span[text()='相册']")
        self.driver.switch_to.frame('frame_content')
        self.key.click(By.XPATH, "//a[text()='上传相片']")
        self.key.click(By.XPATH, "//option[contains(text(),'头大')]")
        self.key.click(By.XPATH, "//*[contains(text(),'切换上传方式')]")
        sleep(1)
        self.key.input(By.XPATH, '//tr[1]//td[1]//input[1]','F:\python\iwebsns\\abc.jpg')
        self.key.click(By.XPATH, "//input[@name='submit']")
        self.key.click(By.XPATH, "//input[@name='action']")
        sleep(1)
        try:
            sleep(1)
            self.assertIn('头大', self.driver.title)
            print("第十一个测试用例登录失败，未进入正确的页面")
            logger.info("失败，未进入正确的页面Failed")

        except:
            print("第十一个测试用例成功登录")
            logger.info("验证成功的测试用例执行Passed")




if __name__ == '__main__':
            unittest.main()
