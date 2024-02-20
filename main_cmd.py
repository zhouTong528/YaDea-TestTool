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
import datetime
import random
import string
import traceback
import threading
import time
from tkinter import font
from jsonpath import jsonpath
# import requests
from Project1_cmd import request_api
def Form_1_onLoad(uiName):
    try:
        # 获取token
        token = Fun.GetUserData('Project1', 'Form_1', 'token')
        # 显示env环境
        env = Fun.GetUserData('Project1', 'Form_1', 'value')
        Fun.SetText(uiName, "env显示", env)
    
        # 获取 tenantID
        if env == 'prod':
            env = ''
    
        host = rf'https://dms{env}.yadea.com.cn'
        api = r'/yd-system/sys/users/current'
        header = {'Authorization': token}
        url = host + api
        res = request_api('get', url=url, headers=header)
        print(res)
        # 获取账号+name,全局访问
        buCode = next(iter(jsonpath(res,'$..username')),None)
        firstName = next(iter(jsonpath(res,'$..firstName')),None)
        print(buCode,firstName)
        Fun.AddUserData(uiName, 'Form_1', dataName='buCode', datatype='string', datavalue=buCode, isMapToText=0)
        Fun.AddUserData(uiName, 'Form_1', dataName='firstName', datatype='string', datavalue=firstName, isMapToText=0)
        # 设置显示
        Fun.SetText(uiName,"acc",buCode)
        Fun.SetText(uiName,'name',firstName)
        roles = jsonpath(res,'$..roles')
        jueSeList = jsonpath(roles,'$..name')
        jueSe = ', '.join(jueSeList)
        Fun.SetText(uiName,"Label_9",jueSe)
    
        # 租户ID
        tenantId = next(iter(jsonpath(res,'$..tenantId')),None)
        Fun.AddUserData(uiName, 'Form_1', dataName='tenantId', datatype='string', datavalue=tenantId, isMapToText=0)
        # 设置显示
        Fun.SetText(uiName,"Label_11",tenantId)
        

        # 门店列表
        store = jsonpath(res, '$..authorizeScopes')
        store = [store['objCode'] + '/' + store['objName'] + '/' + str(store['objId']) for store in store[0]]
        print(store)
        Fun.SetValueList(uiName, "门店下拉框", store)
        Fun.SetCurrentValue(uiName, "门店下拉框", store[0])

    except Exception as Ex:
        print(Ex)
        print("错误详细信息：", traceback.format_exc())
        Fun.MessageBox(text='API：/yd-system/sys/users/current,登录账号门店信息获取失败', title='提示', type='error', parent=None)
    # Fun.LoadUIDialog(uiName,'Frame_2','dianShang_win')



# Button '访问云销通's Event :Command
#Button '访问云销通's Event :Command
def Button_1_onCommand(uiName,widgetName):
    import webbrowser
    env = Fun.GetUserData('Project1', 'Form_1', 'value')
    if env == 'prod':
        env = ''
    webbrowser.open(f'https://dms{env}.yadea.com.cn/login')


# Button '切换账号's Event :Command
#Button '切换账号's Event :Command
def 切换账号_onCommand(uiName,widgetName):
    Fun.GoToUIDialog(uiName, "Project1")
    pass


def 门店下拉框_onSelect(event,uiName,widgetName):
    Fun.MessageBox(text='切换门店后，请重新进入菜单！否则切换失败！', title='提示', type='info', parent=None)


def 导航栏_onItemSelect(uiName,widgetName,itemText,itemValue):
    Fun.LoadUIDialog(uiName, 'Frame_2', itemValue)


def Menu_检查(uiName, itemName):
    Fun.MessageBox(text='当前版本：V1.0.0\n制作者：Test-周通', title='提示', type='info', parent=None)


def get_store(uiName):
    store = Fun.GetCurrentValue(uiName, "门店下拉框")
    return store
