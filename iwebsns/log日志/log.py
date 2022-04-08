#!/usr/bin/env python
# encoding: utf-8
'''
  @author: zxl
  @file: log.py
  @time: 2022/3/29 10:38
  @desc:
'''

import logging
from config配置.config import log_path

#定义日志装置
logger=logging.getLogger()
#设置日志的记录的级别INFO，ERROR，DEBUG,WARNING
logger.setLevel(logging.INFO)
#设置记录的格式
format=logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
logfile=log_path
f=logging.FileHandler(logfile,mode='a',encoding='utf-8')
f.setLevel(logging.INFO)
f.setFormatter(format)
logger.addHandler(f)
##format的参数
# %(name)s :logger的名字
# %(levelno)s:数字形式的日志级别
# %(levelname)s :文本形式的日志级别
# %(pathname)s :调用日志输出函数的模块的路径名
# %(filename)s : 调用日志输出函数的模块文件名
# %(asctime)s :字符串形式显示当前时间，2022-03-29
# %(message)s : 用户输出的消息
# %(lineno)d :日志输出函数的语句所在的代码行
# %(funcName)s :调用日志输出函数的函数名