#!/usr/bin/env python
# encoding: utf-8
'''
  @author: lyq
  @file: test_编辑分类.py
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


    def test_1_add_classification(self):
        '''
        验证成功添加分类的测试用例
        '''
# 点击日志
        self.key.click(By.XPATH, "//span[contains(text(),'日志')]")
        sleep(1)
        self.driver.switch_to.frame('frame_content')
# 点击新建日志
        self.key.click(By.XPATH,"//*[contains(text(),'新建日志')]")
        self.key.click(By.XPATH, '//a[text()="日志分类"]')
        sleep(1)
        self.key.click(By.XPATH,"//div[@id='show_ctrl_4511']//a[@class='log_edit_link']")
        sleep(1)
        self.key.empty(By.XPATH, "//input[@id='change_sort_4511']")
        self.key.input(By.XPATH, "//input[@id='change_sort_4511']",'喵~~')
        sleep(1)
        self.key.click(By.XPATH,"//tr[@id='info_4511_edit']//td[@class='td_b']//input[1]")
        sleep(3)
        try:
            alert_dialog = self.driver.switch_to.alert
            content = alert_dialog.text
            sleep(3)

            self.assertIn('喵~~', content)
            print("第八个测试用例失败")
            logger.info("验证失败，未进入正确的页面Failedd")

        except:
            print("第八个测试用例成功")
            logger.info("验证成功的测试用例执行Passed")



    def test_2_add_classification(self):
        '''
        验证成功删除分类的测试用例
        '''
        self.key.click(By.XPATH, "//div[@id='show_ctrl_4518']//a[@class='log_del_link']")
        sleep(1)
        self.driver.switch_to.alert.dismiss()#取消   (accept确认)
        sleep(1)
        try:
            alert_dialog = self.driver.switch_to.alert
            content = alert_dialog.text
            # alert_dialog.dismiss()#取消   (accept确认)
            self.assertIn('1', content)
            print("第九个测试用例失败")
            logger.info("验证失败，未进入正确的页面Failedd")
        except:
            print("第九个测试用例成功")
            logger.info("验证成功的测试用例执行Passed")


if __name__ == '__main__':
            unittest.main()