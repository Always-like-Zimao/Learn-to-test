#!/usr/bin/env python
# encoding: utf-8
'''
  @author: lyq
  @file: 登录和登出_objects.py
  @time: 2022/3/31  16:28
  @desc:
'''
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self,driver):
        self.user_elem = By.ID, 'login_email'#账号元素
        self.pass_elem = By.ID, 'login_pws'#密码元素
        self.logbutton_elem = By.ID, 'loginsubm'#登录元素
        self.logout_elem = By.LINK_TEXT, '退出'#退出元素
        self.mypage_elem= By.LINK_TEXT,'我的主页'
        self.driver = driver


    def input_username(self, username):#输入账号
        self.driver.find_element(*self.user_elem).clear()
        self.driver.find_element(*self.user_elem).send_keys(username)

    def input_password(self, password):#输入密码
        self.driver.find_element(*self.pass_elem).clear()
        if password == None:#当密码为空是输入空格
            password = ' '
        self.driver.find_element(*self.pass_elem).send_keys(password)

    def click_login(self):#点击登录
        self.driver.find_element(*self.logbutton_elem).click()

    def logout(self):#登出
        self.driver.find_element(*self.logout_elem).click()

    def get_link_text(self):
        return self.driver.find_element(*self.mypage_elem).text