#!/usr/bin/env python
# encoding: utf-8
'''
  @author: lyq
  @file: test_创建日志.py
  @time: 2022/3/31  22:28
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


    def test_1_my_log(self):
        '''
        验证成功创建日志的测试用例
        '''
        # value_list = Datas().read_excel(sheetname[1])
        # username = value_list[0][0]
        # password = value_list[0][1]

#点击日志
        self.key.click(By.XPATH, "//span[contains(text(),'日志')]")
        sleep(1)
        self.driver.switch_to.frame('frame_content')
# 点击新建日志
        self.key.click(By.XPATH, "//*[contains(text(),'新建日志')]")
        self.key.input(By.XPATH,'//input[@name="blog_title"]','头大')
        sleep(1)

#选择分类元素
        self.key.click(By.XPATH,'//*[text()="默认分类"]')
        sleep(1)

# 输入标签
        self.key.click(By.XPATH,'//input[@name="tag"]')
        self.key.input(By.XPATH,'//input[@name="tag"]','无')
        sleep(1)

#输入内容
        self.driver.switch_to.frame('KINDEDITORIFRAME')
        self.driver.find_element(By.XPATH,'//body[@id="KINDEDITORBODY"]').click()
        self.driver.find_element(By.XPATH,'//body[@id="KINDEDITORBODY"]').send_keys('用例')
        sleep(1)
#点击确认
        self.driver.switch_to.default_content()
        js = 'var q=document.documentElement.scrollTop =1000'
        self.driver.execute_script(js)
        self.driver.switch_to.frame('frame_content')
        sleep(1)
        self.driver.find_element(By.XPATH,'//input[@value="确定"]').click()
        self.driver.switch_to.default_content()

        try:
           self.assertIn('头大',self.driver.switch_to.alert.text)
           sleep(1)
           print("第六个测试用例失败")
           logger.info("失败，未进入正确的页面Failed")

        except:
            print("第六个测试用例成功")
            logger.info("验证成功的测试用例执行Passed")


if __name__=='__main__':
    unittest.main()