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

import yaml
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
    yaml_path = r'data.yaml'
    if not os.path.isfile(yaml_path):
        return
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    print(data)
    if data == None:
        Fun.MessageBox("暂无数据!","提示")
        return
    api_list = []
    num = 1
    for key,value in data.items():
        name = key
        api = value['api']
        method = value['method']
        kong = (num,name,api,method)
        api_list.append(kong)
        num = num + 1
    def add_list():
        for i in api_list:
            Fun.AddRowText(uiName,"ListView_1",rowIndex='end',values=i)
        
    run_thread = threading.Thread(target=add_list, args=[])
    run_thread.setDaemon(True)
    run_thread.start()






def LabelButton_1_onCommand(uiName,widgetName):
    # 获取选中数据
    rowIndex = Fun.GetSelectedRowIndex(uiName,"ListView_1")
    if rowIndex == -1:
        Fun.MessageBox("请先选择要删除的接口!","提示")
        return
    if Fun.AskBox("提示","是否删除该接口?"):
        key_to_remove = Fun.GetCellText(uiName,"ListView_1",rowIndex=rowIndex,columnIndex=1)
        try:
            def del_api():
                yaml_path = r'data.yaml'
                with open(yaml_path, 'r') as f:
                    data = yaml.safe_load(f)
                # 删除指定key（如果存在）
                if key_to_remove in data:
                    del data[key_to_remove]
                # 将更新后的数据写回yaml文件
                with open(yaml_path, 'w') as f:
                    yaml.dump(data, f)
                    Fun.MessageBox("删除成功!", "提示")
                Fun.DeleteAllRows(uiName, "ListView_1")

                # 重新加载列表
                yaml_path = r'data.yaml'
                with open(yaml_path, 'r') as f:
                    data = yaml.safe_load(f)

                api_list = []
                num = 1
                for key, value in data.items():
                    name = key
                    api = value['api']
                    method = value['method']
                    kong = (num, name, api, method)
                    api_list.append(kong)
                    num = num + 1

                for i in api_list:
                    Fun.AddRowText(uiName, "ListView_1", rowIndex='end', values=i)

            run_thread = threading.Thread(target=del_api, args=[])
            run_thread.setDaemon(True)
            run_thread.start()

        except Exception as e:
            Fun.MessageBox("删除失败!","提示")
            return







