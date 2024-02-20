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

from  tkinter import *
import threading
import numpy as np
import random
import string
from datetime import datetime
from Project1_cmd import request_api
from jsonpath import jsonpath
import re
import time
def Form_1_onLoad(uiName):
    pass



def 配件单_onCommand(uiName,widgetName):
    ask = Fun.AskBox("是否确认", "是否确认推送售后单？")
    if ask:
        store = Fun.GetCurrentValue('main', "门店下拉框")
        store = store.split("/")
        # 获取token
        token = Fun.GetUserData('Project1', 'Form_1', 'token')
        # 显示env环境
        env = Fun.GetUserData('Project1', 'Form_1', 'value')
        if env == 'prod':
            env = ''
        # 发送
        host = rf'https://dms{env}.yadea.com.cn'
        api = r'/yst/ydpur/servicePurPo/newPurPo'
        header = {'Authorization': token}
        url = host + api
        push_time = int(round(time.time() * 1000))
        bu_code = Fun.GetUserData('main', 'Form_1', 'buCode')
        bu_name = Fun.GetUserData('main', 'Form_1', 'firstName')
        # 定义前缀
        prefix = "67"
        # 定义长度为6的随机数字字符串
        random_digits = ''.join(random.choices(string.digits, k=7))
        # 将前缀和随机数字拼接成最终字符串
        after_doc_no = prefix + random_digits
        print(after_doc_no)
        doc_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        json = {
            "PUSHTIME": push_time,
            "RESOURCE": "SAP",
            "INTERFACECODE": "1001",
            "BATCHNO": "SAP100120220622172946",
            "DATA":
                [
                    {
                        "DOCNO": after_doc_no,
                        "BUMAINCODE": bu_code,
                        "BUCODE": bu_code,
                        "BUNAME": bu_name,
                        "STORECODE": store[0],
                        "DOCTIME": doc_time,
                        "QTY": "0.000 ",
                        "AMT": "0.00 ",
                        "SHIPMENTFACTORY": "1101",
                        "SHIPMENTADDR": "",
                        "SHIPMENTCONTACTNAME": "",
                        "SHIPMENTCONTACTTEL": "",
                        "RECVADDR": "河北省承德市隆化县隆化镇下洼子村",
                        "WHCONTACTNAME": "张国明",
                        "WHCONTACTTEL": "13831488158",
                        "DATAREMARK": "云销通实用组件推送",
                        "MODEL": "配件",
                        "PACKING": "整车",
                        "ORDERCODE": "1700329327",
                        "TYPE": "POST",
                        "POSTINGTDATE": ""
                    }
                ],
            "DETAIL":
                [
                    {
                        "DOCNO": after_doc_no,
                        "LINENO": "10",
                        "ITEMCODE": "L1201000277",
                        "ITEMNAME": "锂电/星恒/中/48V/12Ah/锰锂/一线通/3年/GB2+4同口/172×348×101/中文/3.7V/13S1P/黑",
                        "PRICE": "600.00 ",
                        "QTY": "5.000 ",
                        "UOM": "ZZU",
                        "AMT": "3000.00 ",
                        "MANUDATE": "",
                        "DETAILREMARK": "售后单"
                    }
                ],
            "SERIALS":
                [
                    {
                        "DOCNO": after_doc_no,
                        "LINENO": "10",
                        "ITEMCODE": "L1201000277",
                        "SERIALNO": "",
                        "WORKORDERNO": "",
                        "MANUDATE": "",
                        "SERIALDESC": ""
                    }
                ]
        }

        def api():
            res = request_api('post', url=url, headers=header, json=json)
            print(res)
            print(json)
            res_msg = next(iter(jsonpath(res, "$..MESSAGE")), None)
            res_result = res.get('response').get('RESULT', None)
            if res['status_code'] == 200 and res_msg == "推送成功" and res_result == 'TRUE':
                # 文字
                Fun.SetText(uiName,"Label_4",f"推送成功，采购单号：{after_doc_no}")
                # 更换图片
                Fun.SetImage(uiName,"Label_5","微笑.png",True)
                Fun.SetText(uiName,"Label_6","成功者的微笑")
                Fun.MessageBox(f"推送成功！采购单号：{after_doc_no}", '提示')
            else:
                Fun.MessageBox(f"推送失败,{res['response']}", '提示')

        run_thread = threading.Thread(target=api, args=[])
        run_thread.setDaemon(True)
        run_thread.start()




