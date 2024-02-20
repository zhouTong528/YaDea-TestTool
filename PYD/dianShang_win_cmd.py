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
def Form_1_onLoad(uiName):
    Fun.SetText(uiName,"输入数量","1")
    
    store = Fun.GetCurrentValue('main', "门店下拉框")
    store_code = store.split("/")[0]
    store_name = store.split("/")[1]
    store_id = store.split("/")[2]
    
    env = Fun.GetUserData('Project1', 'Form_1', 'value')
    if env == 'prod':
        env = ''
    token = Fun.GetUserData('Project1', 'Form_1', 'token')
    host = rf'https://dms{env}.yadea.com.cn'
    api = r'/yd-inv/invStk/findPage'
    header = {'Authorization': token}
    json = {"size":100,"current":1,"storeIds":[store_id],
            "orders":[{"asc":"true","column":"item_code"}],
            "whStatus":"ACTIVE","createStoreId":store_id,"createStoreCode":store_code,"createStoreName":store_name}
    res = request_api('post',url=host+api,headers=header,json=json)
    res_msg = jsonpath(res,'$..msg')
    if res['status_code'] == 200 and res_msg[0] == '操作成功':
        res_records = jsonpath(res,'$..records')[0]
        #print(res_records)
        invStk = []
        n = 1
        for i in res_records:
            name = i["itemName"]
            code = i['itemCode']
            kuCun = i['ohQty']
            keYong = i['availableQuantity']
            kong = (n,name, code , kuCun, keYong)
            invStk.append(kong)
            n +=1
        
        
        def add():
            for i in invStk:
                Fun.AddRowText(uiName,"ListView_1",rowIndex='end',values=i)
            
        run_thread = threading.Thread(target=add, args=[])
        run_thread.setDaemon(True)
        run_thread.start()
    else:
        Fun.MessageBox(text='获取门店下仓库商品失败！',title='提示',type='error',parent=None)






def LabelButton_2_onCommand(uiName,widgetName):
    item = Fun.GetText(uiName,"展示商品")
    qty = Fun.GetText(uiName,"输入数量")
    amt = Fun.GetText(uiName,"输入价格")
    
    if item == "" or qty == "" or amt == "":
        Fun.MessageBox(text='请输入完整！',title='提示',type='info',parent=None)
    else:
        item_list = item.split('/',1)
        item_name = item_list[1]
        item_code = item_list[0]
        qty = int(qty)
        amt = float(amt)
        ask = Fun.AskBox(title='请确认',text='确认推送电商物流发货订单！')
        if ask:
            env = Fun.GetUserData('Project1', 'Form_1', 'value')
            if env == 'prod':
                env = ''
            token = Fun.GetUserData('Project1', 'Form_1', 'token')
            host = rf'https://dms{env}.yadea.com.cn'
            api = r'/yd-sale/salShipOrder/salShipOrderAdd'
            header = {'Authorization': token}
        
            push_time = int(round(time.time() * 1000))
            doc_data = datetime.today().strftime('%y%m%d')
            doc_no = ''.join(random.choices(string.digits, k=7))
            omsDocNo = 'EB' + doc_data + doc_no
            store = Fun.GetCurrentValue('main', "门店下拉框")
            store = store.split("/")[0]
        
            json = {
                "docType": 0,
                "mobile": "86-18271946826",
                "county": "黄陂区",
                "amt": qty * amt,
                "docNo": "3367339129745681460",
                "custName": "丁仁杰",
                "detailAddr": "湖北省 武汉市 黄陂区 前川街道 武汉建开工程总承包黄陂文旅城项目部 ，000000",
                "docStatus": "0",
                "province": "湖北省",
                "docTime": push_time,
                "cat": "1",
                "tableId": "2010579",
                "salesQty": qty,
                "omsDocNo": omsDocNo,
                "storeCode": store,
                "ifRenew": 1,
                "omsSalShipOrderDetailDTOList": [
                    {
                        "itemCode": item_code,
                        "amt": amt,
                        "itemName": item_name,
                        "qty": qty
                    }
                ]
            }
            res = request_api('post', url=host + api, headers=header, json=json)
            print(res)
            res_msg = jsonpath(res,'$..msg')
            res_success = res.get('response').get('success')
            print(res_success)
            if res['status_code'] == 200 and res_msg[0] == '操作成功' and res_success == True:
                ask = Fun.AskBox(title='提示',text='推送成功！\n是否访问云销通')
                if ask:
                    import webbrowser
                    env = Fun.GetUserData('Project1','Form_1','value')
                    webbrowser.open(f'https://dms{env}.yadea.com.cn/login')
            else:
                Fun.MessageBox(text=f'推送失败！{res_msg[0]}！',title='错误',type='error',parent=None)
        else:
            pass
            
    

def LabelButton_6_onCommand(uiName,widgetName):
    item = Fun.GetText(uiName,"展示商品")
    qty = Fun.GetText(uiName,"输入数量")
    amt = Fun.GetText(uiName,"输入价格")
    
    if item == "" or qty == "" or amt == "":
        Fun.MessageBox(text='请输入完整！',title='提示',type='info',parent=None)
    else:
        iten_list = item.split('/',1)
        item_name = iten_list[1]
        item_code = iten_list[0]
        print(item_name,item_code,'sssssssss')
        qty = int(qty)
        amt = float(amt)
        ask = Fun.AskBox(title='请确认',text='确认推送电商客户自提订单！')
        if ask:
            env = Fun.GetUserData('Project1', 'Form_1', 'value')
            if env == 'prod':
                env = ''
            token = Fun.GetUserData('Project1', 'Form_1', 'token')
            host = rf'https://dms{env}.yadea.com.cn'
            api = r'/yd-sale/salShipOrder/salShipOrderAdd'
            header = {'Authorization': token}
        
            push_time = int(round(time.time() * 1000))
            doc_data = datetime.today().strftime('%y%m%d')
            doc_no = ''.join(random.choices(string.digits, k=7))
            omsDocNo = 'EB' + doc_data + doc_no
            store = Fun.GetCurrentValue('main', "门店下拉框")
            store = store.split("/")[0]
        
            json = {
                "docType": 1,
                "mobile": "17327880102",
                "county": "朝阳区",
                "amt": qty * amt,
                "docNo": "3367339129745681460",
                "custName": "方先生",
                "detailAddr": "北京市朝阳区-故宫-乾清宫",
                "docStatus": "0",
                "province": "北京市",
                "docTime": push_time,
                "cat": "1",
                "tableId": "89767",
                "salesQty": qty,
                "omsDocNo": omsDocNo,
                "storeCode": store,
                "ifRenew": 1,
                "omsSalShipOrderDetailDTOList": [
                    {
                        "itemCode": item_code,
                        "amt": amt,
                        "itemName": item_name,
                        "qty": qty
                    }
                ]
            }
            res = request_api('post', url=host + api, headers=header, json=json)
            print(res)
            res_msg = jsonpath(res,'$..msg')
            res_success = res.get('response').get('success')
            print(res_success)
            if res['status_code'] == 200 and res_msg[0] == '操作成功' and res_success == True:
                ask = Fun.AskBox(title='提示',text='推送成功！\n是否访问云销通')
                if ask:
                    import webbrowser
                    env = Fun.GetUserData('Project1','Form_1','value')
                    webbrowser.open(f'https://dms{env}.yadea.com.cn/login')
            else:
                Fun.MessageBox(text=f'推送失败！{res_msg[0]}！',title='错误',type='error',parent=None)
        else:
            pass

    
    







def ListView_1_onButton1(event,uiName,widgetName):
    rowIndex = Fun.CheckPickedRow(uiName,"ListView_1",event.x,event.y)
    rowTextList = Fun.GetRowTextList(uiName,"ListView_1",rowIndex=rowIndex)
    item = rowTextList[2] + '/' + rowTextList[1]
    Fun.SetText(uiName,"展示商品","")
    Fun.SetText(uiName,"展示商品",item)
    




    
    

def 输入数量_onFocusOut(event,uiName,widgetName):
    text = Fun.GetText(uiName,"输入数量")
    if text.isdigit() or text == '':
        if len(text) >6:
            Fun.SetText(uiName,"输入数量","999999")
        else:
            pass
    else:
        Fun.SetText(uiName,"输入数量","")
        Fun.MessageBox(text='只能输入整数',title='info',type='info',parent=None)

        



    
    









def 输入数量_onKey(event,uiName,widgetName):
    pass
def 输入价格_onTextChanged(uiName,widgetName,text):
    text = Fun.GetText(uiName,"输入价格")
    if text == '':
        pass
    else:
        pattern = r'^\d+(\.\d+)?$'
        ask = bool(re.match(pattern, text))
        if not ask:
            Fun.SetText(uiName,"输入价格","")
            Fun.MessageBox(text='只能输入浮点型',title='info',type='info',parent=None)
        elif ask:
            if len(text) >9:
                Fun.SetText(uiName,"输入价格","999999.99")
            else:
                pice = float(text)
                pice = round(pice, 2)
                str_pice = str(pice)
                Fun.SetText(uiName,"输入价格",str_pice)





















def 输入价格_onKey(event,uiName,widgetName):
    pass







