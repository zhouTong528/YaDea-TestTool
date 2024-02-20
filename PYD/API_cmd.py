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

from collections import defaultdict
import yaml
from Project1_cmd import request_api
import json
import ast
import re
import threading
import numpy as np
import random
import string
from datetime import datetime
from Project1_cmd import request_api
from jsonpath import jsonpath
def Form_1_onLoad(uiName):
    
    def host():
        # host
        env = Fun.GetText('main','env显示')
        if env == 'prod':
            env = ''
        host = rf'https://dms{env}.yadea.com.cn'
        Fun.SetText(uiName,"Entry_2",host)

    run_thread = threading.Thread(target=host, args=[])
    run_thread.setDaemon(True)
    run_thread.start()

    def get_yaml_keys():
        file_path = r'data.yaml'
        keys = []
        # 检查文件是否存在
        if not os.path.isfile(file_path):
            print(f"警告：文件'{file_path}'不存在")
            return keys

        try:
            # 读取yaml文件内容
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)
            # 如果数据不为空且是字典类型，获取所有顶层键
            if isinstance(data, dict) and data:
                keys = list(data.keys())

        except FileNotFoundError:
            print(f"警告：无法找到文件'{file_path}'")

        except yaml.YAMLError as exc:
            print(f"警告：解析'{file_path}'时发生错误: {exc}")
        if keys:
            Fun.SetValueList(uiName,"ComboBox_2",keys)  
        
        
        return keys

    run_thread = threading.Thread(target=get_yaml_keys, args=[])
    run_thread.setDaemon(True)
    run_thread.start()



def 发送_onCommand(uiName,widgetName):
    # host
    host = Fun.GetText(uiName,"Entry_2")
    # api
    api = Fun.GetText(uiName,"Entry_8")
    if api == '':
        Fun.MessageBox(text='请输入api地址！',title='提示',type='info',parent=None)
        return
    url = host + api
    # method
    method = Fun.GetCurrentValue(uiName,"ComboBox_1")
    print(method)
    # header
    header_win = Fun.GetText(uiName,"Entry_7")
    if header_win:
        header_win = ast.literal_eval(header_win)

        if not type(header_win) == dict:
            Fun.MessageBox(text="请求头格式错误！请重新填写字典格式！\n例如：{'account':'123465789' , 'pwd':'888888'}",title='提示',type='info',parent=None)
            return
        
        token = Fun.GetUserData('Project1','Form_1','token')
        token_header = {'Authorization': token}
        
        header = {**header_win, **token_header}
    else:
        token = Fun.GetUserData('Project1','Form_1','token')
        header = {'Authorization': token}
    # 请求体格式
    re_format = Fun.GetCurrentValue(uiName,'RadioButton_1')
    if re_format == 1:
        re_format = 'params'
    elif re_format == 2:
        re_format = 'json'
    elif re_format == 3:
        re_format = 'data'
    print(re_format)
    # 请求body
    body = Fun.GetText(uiName,"Text_1")
    body = body.replace("\n", "")
    #print(body,type(body))
    if body == "":
        body = None
    elif body:
        try:
            body = json.loads(body)
        except Exception as Ex:
            Fun.MessageBox(text='请求body格式错误！请重新填写json格式(双引号)！\n例如：{"account":"123465789" , "pwd":"888888"}',title='提示',type='info',parent=None)
            return
            
    def request():
        if method == 'GET':
            res = request_api(url=url,method=method,headers=header,params=body)
        
        elif method == 'POST':
            if re_format == "json":
                res = request_api(url=url,method=method,headers=header,json=body)
            elif re_format == "data":
                res = request_api(url=url,method=method,headers=header,data=body)
            else:
                Fun.MessageBox(text='POST请求方式，请选择Json/Data',title='提示',type='info',parent=None)
                return
            
        elif method == 'PUT':
                if re_format == "json":
                    res = request_api(url=url,method=method,headers=header,json=body)
                elif re_format == "data":
                    res = request_api(url=url,method=method,headers=header,data=body)
                else:
                    Fun.MessageBox(text='PUT请求方式，请选择Json/Data',title='提示',type='info',parent=None)
                    return
                
    
        elif method == 'DELETE':
                if re_format == "json":
                    res = request_api(url=url,method=method,headers=header,json=body)
                elif re_format == "data":
                    res = request_api(url=url,method=method,headers=header,data=body)
                else:
                    Fun.MessageBox(text='DELETE请求方式，请选择Json/Data',title='提示',type='info',parent=None)
                    return
                    
        Fun.AddUserData(uiName,'Form_1',dataName='res',datatype='dict',datavalue=res,isMapToText=0)
        
        if res == None:
            Fun.MessageBox(text='请求错误！请检查后重试！',title='错误',type='warning',parent=None)
        else:
            def open_win():
                topmost = 1
                toolwindow = 1
                grab_set = 1
                animation = ''
                InputDataArray = Fun.CallUIDialog("response",topmost,toolwindow,grab_set,animation)
        
            run_thread = threading.Thread(target=open_win, args=[])
            run_thread.setDaemon(True)
            run_thread.start()

        
    run_thread = threading.Thread(target=request, args=[])
    run_thread.setDaemon(True)
    run_thread.start()
    

    
    

    
    
    
    
    
    
# 保存
def LabelButton_3_onCommand(uiName,widgetName):
    name = Fun.GetText(uiName,"Entry_10")
    if name == '':
        Fun.MessageBox(text='请输入接口名称！',title='提示',type='info',parent=None)
        return

    method = Fun.GetCurrentValue(uiName,"ComboBox_1")
    api = Fun.GetText(uiName,"Entry_8")
    if api == '':
        Fun.MessageBox(text='请输入api地址！',title='提示',type='info',parent=None)
        return
    value = Fun.GetCurrentValue(uiName,"RadioButton_1")
    if value == 1:
        re_format = 'params'
    elif value == 2:
        re_format = 'json'
    elif value == 3:
        re_format = 'data'
    body = Fun.GetText(uiName,"Text_1")
    body = body.replace("\n", "")
    if body == '':
        body = None

    header = Fun.GetText(uiName,"Entry_7")
    if header == '':
        header = None
    
    # 指定yaml文件路径和要保存的数据
    yaml_file_path = 'data.yaml'
    data_to_save = {name: {'method':method, 'api':api, 're_format':re_format, 'body':body, "headers":header}}  # 要保存的数据的键值对

    # 检查文件是否存在
    if os.path.isfile(yaml_file_path):
        # 文件存在，读取并更新当前内容
        with open(yaml_file_path, 'r') as file:
            existing_data = yaml.safe_load(file)
            for key, value in data_to_save.items():
                existing_data[key] = value
                print(existing_data)

        # 写回更新后的数据到同一文件
        with open(yaml_file_path, 'w') as file:
            yaml.dump(existing_data, file,allow_unicode=True)

        # 读取yaml文件内容
        with open(yaml_file_path, 'r') as file:
            data = yaml.safe_load(file)
        # 如果数据不为空且是字典类型，获取所有顶层键
        keys = []
        if isinstance(data, dict) and data:
            keys = list(data.keys())
        Fun.SetValueList(uiName, "ComboBox_2", keys)

        Fun.MessageBox(text='保存成功！',title='提示',type='info',parent=None)
    else:
        # 文件不存在，新建并保存数据
        with open(yaml_file_path, 'w') as file:
            yaml.dump(data_to_save, file,allow_unicode=True)
        # 读取yaml文件内容
        with open(yaml_file_path, 'r') as file:
            data = yaml.safe_load(file)
        # 如果数据不为空且是字典类型，获取所有顶层键
        keys = []
        if isinstance(data, dict) and data:
            keys = list(data.keys())
        Fun.SetValueList(uiName, "ComboBox_2", keys)
        Fun.MessageBox(text='保存成功！', title='提示', type='info', parent=None)






    
    
    
    
def Entry_3_onKey(event,uiName,widgetName):
    pass


def Entry_4_onKey(event,uiName,widgetName):
    pass


def ComboBox_1_onSelect(event,uiName,widgetName):
    pass
def ComboBox_2_onSelect(event,uiName,widgetName):
    # 当前选择
    api_name = Fun.GetCurrentValue(uiName,"ComboBox_2")
    
    # 读取yaml
    yaml_path = r'data.yaml'
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    api_datas = data.get(api_name)
    method = api_datas.get('method')
    api = api_datas.get('api')
    re_format = api_datas.get('re_format')

    
    Fun.SetText(uiName,"Entry_10",api_name)
    Fun.SetText(uiName,"Entry_8",api)
    Fun.SetCurrentValue(uiName,"ComboBox_1",method)
    if api_datas.get('headers') == None:
        Fun.SetText(uiName,"Entry_7",'')
    else:
        Fun.SetText(uiName,"Entry_7",api_datas.get('headers'))

    if api_datas.get('body') == None:
        Fun.SetText(uiName,"Text_1",'')
    else:
        Fun.SetText(uiName,"Text_1",api_datas.get('body'))

    if re_format == 'params':
        Fun.SetCurrentValue(uiName,"RadioButton_1",1)
    elif re_format == 'json':
        Fun.SetCurrentValue(uiName,"RadioButton_1",2)
    elif re_format == 'data':
        Fun.SetCurrentValue(uiName,"RadioButton_1",3)
    
    
    
    
    
    
    
    
#RadioButton 'Params's Event :Command
def RadioButton_1_onCommand(uiName,widgetName):
    pass



#RadioButton 'Data's Event :Command
def RadioButton_3_onCommand(uiName,widgetName):
    pass

















def Text_1_onKey(event,uiName,widgetName):
    pass





































































