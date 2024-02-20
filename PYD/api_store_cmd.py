#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

# coding=utf-8
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(__file__)))
from tkinter import *
ElementBGArray = {}
ElementBGArray_Resize = {}
ElementBGArray_IM = {}
# coding=utf-8
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(__file__)))
from tkinter import *
ElementBGArray = {}
ElementBGArray_Resize = {}
ElementBGArray_IM = {}
import re
import threading
from jsonpath import jsonpath
import numpy as np
# coding=utf-8
import time
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(__file__)))
from tkinter import *
ElementBGArray = {}
ElementBGArray_Resize = {}
ElementBGArray_IM = {}
import random
import string
from datetime import datetime
from Project1_cmd import request_api
from jsonpath import jsonpath
import re
def Form_1_onLoad(uiName):
    pass


def Entry_3_onKey(event,uiName,widgetName):
    pass


def 编码_onTextChanged(uiName,widgetName,text):
    code = Fun.GetText(uiName, "编码")
    pattern = r'^[a-zA-Z0-9]+$'
    ask = bool(re.match(pattern, code))
    if not ask:
        Fun.SetText(uiName, "编码", "")
        Fun.MessageBox(text='门店编号只能输入字母+数字！请重新输入！', title='提示', type='info', parent=None)
    else:
        pass


def Entry_4_onKey(event,uiName,widgetName):
    pass


def 名称_onTextChanged(uiName,widgetName,text):
    name = Fun.GetText(uiName, "名称")
    pattern = r'^[a-zA-Z0-9\u4e00-\u9fa5]+$'
    ask = bool(re.match(pattern, name))
    if not ask:
        Fun.SetText(uiName, "名称", "")
        Fun.MessageBox(text='门店名称只能输入中文+字母+数字！请重新输入！', title='提示', type='info', parent=None)
    else:
        pass


def ComboBox_10_onSelect(event,uiName,widgetName):
    pass


def LabelButton_3_onCommand(uiName,widgetName):
    code = Fun.GetText(uiName, "编码")
    name = Fun.GetText(uiName, "名称")
    if code == "" or name == '':
        Fun.MessageBox(text='请先完善信息！', title='提示', type='info', parent=None)
    else:
        ask = Fun.AskBox(title='请确认',text='确认要新增门店？')
        if ask:
            cat = Fun.GetCurrentValue(uiName, "级别")
            ifHead = Fun.GetCurrentValue(uiName, "是否总店")
            storeType = Fun.GetCurrentValue(uiName, "类型")
            storeStatus = Fun.GetCurrentValue(uiName, "状态")
            dict1 = {
                '级别': {'一网': '1', '二网': '2'},
                '是否总店': {'是': 1, '否': 0},
                '类型': {'销售店': 'A', '综合店': 'C', '服务站':'B', '服务体验中心':'D', '雅迪销售店': 'E', '雅迪综合店':'F'},
                '状态': {'启用': "ACTIVE", '禁用': 'CLOSED'}
            }
            cat = dict1.get('级别').get(cat)
            ifHead = dict1.get('是否总店').get(ifHead)
            storeType = dict1.get('类型').get(storeType)
            storeStatus = dict1.get('状态').get(storeStatus)

            buCode = Fun.GetUserData('main','Form_1','buCode')
            buName = Fun.GetUserData('main','Form_1','firstName')
            
            env = Fun.GetUserData('Project1', 'Form_1', 'value')
            if env == 'prod':
                env = ''
            token = Fun.GetUserData('Project1', 'Form_1', 'token')
            host = rf'https://dms{env}.yadea.com.cn'
            api = r'/yd-user/orgStoreChannel/pushStore'
            header = {'Authorization': token}
            json = [
                {
                    "storeCode": code,
                    "storeName": name,
                    "buCode": buCode,
                    "buName": buName,
                    "cat23": "15637966098",
                    "cat": cat,
                    "ifHead": ifHead,
                    "storeType": storeType,
                    "addrDefaultDTO": {
                        "country": "中国",
                        "mobile": "15637966098",
                        "province": "河南省",
                        "city": "洛阳市",
                        "county": "涧西区",
                        "contPerson": "杨伙华"
                    },
                    "storeStatus": storeStatus,
                    "region": "豫北",
                    "regionCode": "11"
                }
            ]

            
            def request():
                try:
                    res = request_api('post', url=host+api, headers=header ,json=json)
                    print(json)
                    print(res)
                    res_msg = jsonpath(res,'$..msg')

                    res_success = res.get('response').get('success')
                    if res['status_code'] == 200 and res_msg[0] == '操作成功' and res_success == True:
                        Fun.MessageBox(text='新增成功！',title='提示',type='info',parent=None)
                    else:
                        Fun.MessageBox(text=f'推送失败！{res_msg[0]}！',title='错误',type='error',parent=None)
                except Exception as Ex:
                    print(json)
                    print(res)
                    print(Ex)

            run_thread = threading.Thread(target=request, args=[])
            run_thread.setDaemon(True)
            run_thread.start()
        else:
            pass
            
        










