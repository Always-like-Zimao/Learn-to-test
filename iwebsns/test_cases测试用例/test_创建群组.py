#!/usr/bin/env python
# encoding: utf-8
'''
  @author: lyq
  @file: test_创建群组.py
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


    def test_1_create_group(self):
        '''
        验证成功创建群组的测试用例
        '''
        self.key.click(By.XPATH,"//span[text()='群组']")
        self.driver.switch_to.frame('frame_content')
        self.key.click(By.XPATH, "//a[text()='创建群组']")
# 名称
        self.key.input(By.XPATH,"//input[@id='group_name']",'起名字好麻烦')
# 群组介绍
        self.key.input(By.XPATH,"//textarea[@id='group_resume']",'起名字好麻烦啊')
# 加入方式
        self.key.click(By.XPATH,"//option[text()='自由加入']")
# 标签
        self.key.input(By.XPATH,"//input[@type='text' and @class='small-text']",'起名字好麻烦')
# 类别
        self.key.click(By.XPATH,"//option[text()='游戏动漫']")
# 创建
        self.key.click(By.XPATH, "//input[@id='UploadButton']")
        sleep(1)

        try:
            sleep(3)
            self.assertIn('起名字好麻烦', self.driver.switch_to.alert.text)
            print("第十二个测试用例失败")
            logger.info("失败，未进入正确的页面Failed")

        except:
            print("第十二个测试用例成功")
            logger.info("验证成功的测试用例执行Passed")

if __name__ == '__main__':
            unittest.main()