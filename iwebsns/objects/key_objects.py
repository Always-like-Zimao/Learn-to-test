#!/usr/bin/env python
# encoding: utf-8
'''
  @author: lyq
  @file: key_objects.py
  @time: 2022/4/1  21:45
  @desc:
'''
from time import sleep
class Key:
    def __init__(self, driver):
        self.driver = driver

    #输入
    def input(self,name,value,txt):
        self.driver.find_element(name,value).send_keys(txt)

    #点击
    def click(self,name,value):
        self.driver.find_element(name,value).click()

    #等待
    def wait(self,time_):
        sleep(time_)

    #清空
    def empty(self,name,value):
        self.driver.find_element(name,value).clear()

    #选择
    def select(self,name,value):
        self.driver.find_element(name, value).Select()