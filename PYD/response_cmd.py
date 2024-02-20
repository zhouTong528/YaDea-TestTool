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
    # 响应体
    res = Fun.GetUserData('API','Form_1','res')
    response = res.get('response')
    Fun.SetText(uiName,"Text_1",response)
    
    # 响应码
    status_code = res.get('status_code')
    Fun.SetText(uiName,"Label_3",status_code)









