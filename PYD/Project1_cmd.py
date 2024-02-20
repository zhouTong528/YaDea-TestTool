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

import threading
import requests
import base64
import requests
from jsonpath import jsonpath
import traceback
def Form_1_onLoad(uiName):
    pass

def Form_1_onInitCheck(uiName):
    def get_pwd():
        text = '123'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}  # 设置爬虫头部，伪装成浏览器
        # url，网址
        url = 'https://tibiji.com/yadea'
        res = requests.get(url, headers=headers)
        res.encoding = res.apparent_encoding
        if res.text.find(text) > 0:
            pass
        else :
            Fun.MessageBox(text='版本已过期！',title='错误',type='warning',parent=None)
            Fun.DestroyUI('Project1')
    run_thread = threading.Thread(target=get_pwd, args=[])
    run_thread.setDaemon(True)
    run_thread.start()

    
def login_onCommand(uiName,widgetName):
    value = Fun.GetCurrentValue(uiName,"ComboBox_1")
    #print(value,'sss')
    Fun.AddUserData(uiName,'Form_1',dataName='value',datatype='string',datavalue=value,isMapToText=0)
    account = Fun.GetText(uiName,"Entry_2")
    pwd = Fun.GetText(uiName,"密码")
    
    if not account:
        Fun.MessageBox(text='请输入登录账号！',title='提示',type='warning',parent=None)
    elif not pwd:
        Fun.MessageBox(text='请输入密码！',title='提示',type='warning',parent=None)
    else:
        if value == "prod":
            value = ''

        host = rf'https://dms{value}.yadea.com.cn'
        api = r'/auth/oauth/token'
        url = host + api
        print(url)
        pwd = base64.b64encode(pwd.encode()).decode()
        data = {'username': account, 'password': pwd, 'captcha': 1, 'capuid':'undefined', 'client_id': 'pc',
                'client_secret':123456, 'grant_type':'password', 'scope':'all'}
        res_login = request_api('post',url=url,data=data)
        print(res_login)

        res_mg = jsonpath(res_login, '$..msg')
        if res_login["status_code"]==200 and res_mg[0] == '操作成功':
            access_token = jsonpath(res_login, '$..access_token')
            if access_token == False:
                Fun.MessageBox(text='jsonpath 未匹配到token，请检查jsonpath表达式',title='提示',type='warning',parent=None)
                raise TypeError('jsonpath 未匹配到token，请检查jsonpath表达式')

            else:
                token = 'bearer ' + access_token[0]
                Fun.AddUserData(uiName,'Form_1',dataName='token',datatype='string',datavalue=token,isMapToText=0)
                Fun.MessageBox(text='登录成功！',title='提示',type='info',parent=None)
                Fun.GoToUIDialog(uiName,"main")
                
        elif res_login["status_code"] == 200:
            Fun.MessageBox(text=res_mg[0],title='提示',type='error',parent=None)
                 
        elif res_login["status_code"] != 200:
            Fun.MessageBox(text=f'响应码：{res_login["status_code"]}\n错误信息：{res_login["response"]["error"]}',title='提示',type='info',parent=None)
            text = '登录接口返回数据：  ' + str(res_login)

            


    
        

    
def 密码_onKey_Return(event,uiName,widgetName):
    login_onCommand(uiName,widgetName)

def 密码_onKey(event,uiName,widgetName):
    pass
def ComboBox_1_onKey_Return(event,uiName,widgetName):
    login_onCommand(uiName,widgetName)




def tuichu(uiName,itemName):
    root = Fun.GetElement(uiName,'root')
    sysTray = Fun.GetElement(uiName,'SysTray')
    Fun.DestroyUI(uiName)
    sysTray.exit()



def request_api(method,url,headers=None,params=None,json=None,data=None):
    response_dict = {}
    if method in ['get', 'GET']:
        try:
            res = requests.get(url=url, params=params, headers=headers)
            # 获取响应头，查看返回数据的格式
            res_headers = res.headers
            headers_type = res_headers.get('Content-Type')
            if headers_type == 'application/json':
                response = res.json()
            else:
                response = res.text
            # 获取响应码
            status_code = res.status_code
            # 加入response_dict字典返回出去
            response_dict['status_code'] = status_code
            response_dict['response'] = response
            return response_dict
        except Exception as e:
            error_info = traceback.format_exc()
    elif method in ['post', 'POST']:
        try:
            res = requests.post(url=url, params=params, headers=headers, json=json, data=data)
            # 获取响应头，查看返回数据的格式
            res_headers = res.headers
            headers_type = res_headers.get('Content-Type')
            if headers_type == 'application/json':
                response = res.json()
            else:
                response = res.text
            # 获取响应码
            status_code = res.status_code
            # 加入response_dict字典返回出去
            response_dict['status_code'] = status_code
            response_dict['response'] = response
            return response_dict
        except Exception as e:
            print(e)
