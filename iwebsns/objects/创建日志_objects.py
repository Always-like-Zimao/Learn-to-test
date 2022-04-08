#!/usr/bin/env python
# encoding: utf-8
'''
  @author: lyq
  @file: 创建日志_objects.py
  @time: 2022/3/31  16:28
  @desc:
'''
from selenium.webdriver.common.by import By
class MyLog:
    def __init__(self,driver):
        self.log_elem=By.XPATH, "//span[contains(text(),'日志')]"
        self.new_log_elem=By.XPATH, "//*[contains(text(),'新建日志')]"
        self.title_elem=By.XPATH,'//input[@name="blog_title"]'#标题元素
        self.classification_elem=By.XPATH,'//*[text()="默认分类"]'#分类元素
        self.choose_classification_elem=By.LINK_TEXT,'乌拉'#选择分类元素
        self.enter_label_elem=By.CLASS_NAME,'med-text'#标签元素
        self.content_elem=By.ID,'KINDEDITORBODY'#内容元素
        self.determine_elem=By.LINK_TEXT,'确定'
        self.driver = driver

    def click_log(self):#点击日志
        self.driver.find_element(self.log_elem).click()

    def click_new_log(self):#点击新建日志
        self.driver.find_element(self.new_log_elem).click()

    def title(self,title1):#输入标题
        self.driver.find_element(self.title_elem).click()
        self.driver.find_element(*self.title_elem).send_keys(title1)

    def classification(self):#选择分类
        self.driver.find_element(self.classification_elem).click()
        self.driver.find_element(self.choose_classification_elem).click()
    def add_classification(self,add):#添加分类
        pass

    def label(self,label1):#输入标签
        self.driver.find_element(self.enter_label_elem).click()
        self.driver.find_element(self.enter_label_elem).send_keys(label1)

    def input_content(self,content):#输入内容
        self.driver.find_element(self.content_elem).click()
        self.driver.find_element(self.content_elem).send_keys(content)

    def click_affirm(self):#点击确认
        self.driver.find_element(self.determine_elem).click()