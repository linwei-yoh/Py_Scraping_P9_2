#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

'''P9.2 提交一个基本表单'''
params = {'firstname':'AL','lastname':'Lin'}

'''处理表单的地址 可以再chrome中F12到调试界面，
选择network标签,点击登录,观察network下提交地址与提交方式'''
r = requests.post("http://pythonscraping.com/pages/files/processing.php",data=params)
print(r.text)
