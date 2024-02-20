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
import threading
import numpy as np
import time
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(__file__)))
import random
import string
from datetime import datetime
from Project1_cmd import request_api
from jsonpath import jsonpath
import re
def Form_1_onLoad(uiName):
    pass


def 整车单_onCommand(uiName,widgetName):
    ask = Fun.AskBox("是否确认", "是否确认推送整车单？")
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
        prefix = "66"
        # 定义长度为6的随机数字字符串
        random_digits = ''.join(random.choices(string.digits, k=6))
        # 将前缀和随机数字拼接成最终字符串
        all_doc_no = prefix + random_digits
        print(all_doc_no)
        doc_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        json = {
            "PUSHTIME": push_time,
            "RESOURCE": "SAP",
            "INTERFACECODE": "1001",
            "BATCHNO": "SAP10012021121311013",
            "DATA": [{
                "DOCNO": all_doc_no,
                "BUMAINCODE": bu_code,
                "BUCODE": bu_code,
                "BUNAME": bu_name,
                "STORECODE": store[0],
                "DOCTIME": doc_time,
                "QTY": "0.000 ",
                "AMT": "0.00 ",
                "SHIPMENTFACTORY": "1001",
                "SHIPMENTADDR": "",
                "SHIPMENTCONTACTNAME": "",
                "SHIPMENTCONTACTTEL": "",
                "RECVADDR": "浙江省温州市经济开发区滨海4道5",
                "WHCONTACTNAME": "苏照合",
                "WHCONTACTTEL": "15864685111",
                "DATAREMARK": "云销通实用组件推送",
                "MODEL": "整车",
                "PACKING": "散车",
                "ORDERCODE": "1000002204"
            }],
            "DETAIL": [{
                "DOCNO": all_doc_no,
                "LINENO": "10",
                "ITEMCODE": "G006-0H01A40-W1801",
                "ITEMNAME": "冠能魅影DM630-D-豪华版前碟AC-W—米杏白/晴空白（Q+HK）TT",
                "PRICE": "2480.00 ",
                "QTY": "1.000 ",
                "UOM": "ZPC",
                "AMT": "2480.00 ",
                "MANUDATE": "",
                "DETAILREMARK": "整车单"
            },
                {
                    "DOCNO": all_doc_no,
                    "LINENO": "10",
                    "ITEMCODE": "G006-0H01A40-W1801",
                    "ITEMNAME": "冠能魅影DM630-D-豪华版前碟AC-W—米杏白/晴空白（Q+HK）TT",
                    "PRICE": "2480.00 ",
                    "QTY": "1.000 ",
                    "UOM": "ZPC",
                    "AMT": "2480.00 ",
                    "MANUDATE": "",
                    "DETAILREMARK": "整车单"
                }
            ],
            "SERIALS": [{
                "DOCNO": all_doc_no,
                "LINENO": "10",
                "ITEMCODE": "G006-0H01A40-W1801",
                "SERIALNO": "779422310431892",
                "WORKORDERNO": "2000000453",
                "MANUDATE": "",
                "SERIALDESC": ""
            },

                {"DOCNO": all_doc_no,
                 "LINENO": "10",
                 "ITEMCODE": "G006-0H01A40-W1801",
                 "SERIALNO": "779422310431651",
                 "WORKORDERNO": "2000000453",
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
                # 设置文字
                Fun.SetText(uiName,"文字",f"推送成功，采购单号：{all_doc_no}")
                Fun.SetElementVisible(uiName,"Label_6",False)
                # 更换图片
                Fun.SetImage(uiName,"头秃","拿下.png",True)
                Fun.MessageBox(f"推送成功！采购单号：{all_doc_no}", '提示')
            else:
                Fun.MessageBox(f"推送失败,{res['response']}", '提示')

        run_thread = threading.Thread(target=api, args=[])
        run_thread.setDaemon(True)
        run_thread.start()


def 随车单_onCommand(uiName,widgetName):
    ask = Fun.AskBox("是否确认", "是否确认推送随车单？")
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
        prefix = "66"
        # 定义长度为7的随机数字字符串
        random_digits = ''.join(random.choices(string.digits, k=7))
        # 将前缀和随机数字拼接成最终字符串
        follow_doc_no = prefix + random_digits
        print(follow_doc_no)
        doc_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        json = {
            "PUSHTIME": push_time,
            "RESOURCE": "SAP",
            "INTERFACECODE": "1001",
            "BATCHNO": "SAP100120220622172946",
            "DATA":
                [
                    {
                        "DOCNO": follow_doc_no,
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
                        "DOCNO": follow_doc_no,
                        "LINENO": "10",
                        "ITEMCODE": "L8050001117",
                        "ITEMNAME": "后靠背垫/C13E/轻奢棕/两面弹/660×275/防滑面/有标",
                        "PRICE": "50.00 ",
                        "QTY": "5.000 ",
                        "UOM": "ZZU",
                        "AMT": "250.00 ",
                        "MANUDATE": "",
                        "DETAILREMARK": "随车单"
                    }
                ],
            "SERIALS":
                [
                    {
                        "DOCNO": follow_doc_no,
                        "LINENO": "10",
                        "ITEMCODE": "L8050001117",
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
                # 隐藏文字
                Fun.SetText(uiName,"文字",f"推送成功，采购单号：{follow_doc_no}")
                # 更换图片
                Fun.SetImage(uiName,"头秃","微笑.png",True)
                Fun.SetText(uiName,"Label_6","成功者的微笑")
                Fun.MessageBox(f"推送成功！采购单号：{follow_doc_no}", '提示')
                
            else:
                Fun.MessageBox(f"推送失败,{res['response']}", '提示')

        run_thread = threading.Thread(target=api, args=[])
        run_thread.setDaemon(True)
        run_thread.start()







