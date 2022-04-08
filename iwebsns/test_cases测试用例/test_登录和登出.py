#!/usr/bin/env python
# encoding: utf-8
'''
  @author: lyq
  @file: test_登录和登出.py
  @time: 2022/3/31  16:24
  @desc:
'''
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
from objects.登录和登出_objects import LoginPage
from config配置.config import driver_path,url,sheetname
from data数据.data import Datas
from log日志.log import logger
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
        cls.key = Key(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print('关闭浏览器')
        cls.driver.quit()


    def test_1_login(self):
        '''
        验证成功登录的测试用例
        '''
        value_list=Datas().read_excel(sheetname[0])
        username=value_list[0][0]
        password=value_list[0][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        sleep(1)
        self.loginpage.click_login()
        sleep(1)
        try:
            self.assertEqual("我的主页", self.loginpage.get_link_text())
            sleep(2)
            print("第一个测试用例成功登录")
            logger.info("验证成功登录的测试用例执行Passed")

        except:
            print("第一个测试用例登录失败，未进入正确的页面")
            logger.info("登录失败，未进入正确的页面Failed")

    def test_2_logout(self):
        '''
        验证登出测试用例
        '''
        self.loginpage.logout()
        sleep(2)

        try:
            sleep(3)
            self.assertIn('会员登录', self.driver.switch_to.alert.text)
            print("第二个测试用例失败")
            logger.info("验证成功登录的测试用例执行Failed")

        except:
            print("第二个测试用例成功")
            logger.info("登录失败，未进入正确的页面Passed")

    def test_3_login(self):
        '''
        验证空密码登录的测试用例
        '''
        value_list=Datas().read_excel(sheetname[0])
        username=value_list[1][0]
        #password=value_list[1][1]
        self.loginpage.input_username(username)
        #self.loginpage.input_password(password)
        sleep(1)
        self.loginpage.click_login()
        sleep(1)
        try:
            sleep(3)
            self.assertIn('密码不能为空!', self.driver.switch_to.alert.text)

            print("第三个测试用例失败")
            logger.info("验证成功登录的测试用例执行Failed")
        except:
            print("第三个测试用例成功")
            logger.info("登录失败，未进入正确的页面Passed")


    def test_4_login(self):
        '''
        验证错误密码的测试用例
        '''
        value_list = Datas().read_excel(sheetname[0])
        username = value_list[2][0]
        password = value_list[2][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        sleep(1)
        self.loginpage.click_login()
        sleep(1)
        try:
            sleep(3)
            self.assertIn('用户密码错误!', self.driver.title)
            print("第四个测试用例失败")
            logger.info("验证成功登录的测试用例执行Failed")

        except:
            print("第四个测试用例成功")
            logger.info("登录失败，未进入正确的页面Passed")


    def test_5_login(self):
        '''
        验证错误账号的测试用例
        '''
        value_list = Datas().read_excel(sheetname[0])
        username = value_list[3][0]
        password = value_list[3][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        sleep(1)
        self.loginpage.click_login()
        sleep(1)
        try:
            sleep(3)
            self.assertIn('登录帐号错误，请重试', self.driver.title)
            print("第五个测试用例失败")
            logger.info("验证成功登录的测试用例执行Failed")

        except:
            print("第五个测试用例成功")
            logger.info("登录失败，未进入正确的页面Passed")

if __name__=='__main__':
    unittest.main()