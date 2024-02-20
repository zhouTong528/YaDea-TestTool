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

import concurrent.futures
import threading
import chromedriver_autoinstaller
import winreg
import time
def LabelButton_1_onCommand(uiName,widgetName):
    # 通过注册表的方式获取Google Chrome的版本
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Google\Chrome\BLBeacon')
        version, types = winreg.QueryValueEx(key, 'version')
        print("本机目前的Chrome版本为:", version)
        Fun.SetText(uiName,"Label_4",version)
    except:
        Fun.MessageBox(text='获取失败',title='提示',type='error',parent=None)
    
    
    
def LabelButton_5_onCommand(uiName,widgetName):
    # 查询系统内的Chromedriver版本
    try:
        def version():
            ChromeDriverVersion = os.popen('chromedriver --version').read()
            driverVersion = ChromeDriverVersion.split(' ')[1]
            print(type(ChromeDriverVersion))
            print("本机目前的Chromedriver版本为:", driverVersion)
            Fun.SetText(uiName,"driver",driverVersion)
        run_thread = threading.Thread(target=version, args=[])
        run_thread.setDaemon(True)
        run_thread.start()

    except Exception as Ex:
        Fun.MessageBox(text='获取失败!\n只会在Python目录中查询',title='提示',type='error',parent=None)
        
    pass





    
    
    
    
    
    
    
    
    

def LabelButton_6_onCommand(uiName,widgetName):
    openPath = Fun.SelectDirectory(title='打开目录查找',initDir=os.path.abspath('.'))
    openPath = openPath.replace('/','\\')
    Fun.SetText(uiName,"路径",openPath)
    
    


def 下载114前_onCommand(uiName,widgetName):
    ask = Fun.AskBox(title='提示',text='需要手动下载，点击是自动打开网站')
    if ask:
        import webbrowser
        webbrowser.open('https://registry.npmmirror.com/binary.html?path=chromedriver/')
    else:
        pass
        

def 下载最新_onCommand(uiName,widgetName):
    text = Fun.GetText(uiName,'路径')
    ask = Fun.AskBox(title='请确认',text='请确认是否要下载最新ChromeDriver驱动？')
    if ask: 
        if len(text) == 0:
            Fun.MessageBox(text='请选择下载路径！',title='提示',type='warning',parent=None)
        elif not Fun.CheckExist(text):
            Fun.MessageBox(text='选择的路径不存在！请重新选择目录！',title='提示',type='error',parent=None)
        elif Fun.CheckExist(text):
            def down_driver():
                try:
                    path = chromedriver_autoinstaller.install(path=text)
                    if path:
                        for i in range(90,100,1):
                            Fun.SetCurrentValue(uiName,"Progress_3",i)
                            time.sleep(0.1)
                        Fun.SetElementVisible(uiName,"Progress_3",False)
                        Fun.SetElementVisible(uiName,"下载最新",True)
                        Fun.MessageBox(text='下载成功！',title='提示',type='info',parent=None)
                        # 打开文件目录
                        dir_path = os.path.dirname(path)
                        os.startfile(dir_path)
                        return path
                    else:
                        Fun.SetElementVisible(uiName,"Progress_3",False)
                        Fun.SetElementVisible(uiName,"下载最新",True)
                        Fun.MessageBox(text='下载失败！',title='提示',type='warning',parent=None)

                except Exception as Ex:
                    Fun.SetElementVisible(uiName,"Progress_3",False)
                    Fun.SetElementVisible(uiName,"下载最新",True)
                    Fun.MessageBox(text=Ex,title='提示',type='warning',parent=None)
                    

            try:
                def close():
                    Fun.SetElementVisible(uiName,"下载最新",False)
                # 关闭按钮展示
                run_thread = threading.Thread(target=close, args=[])
                run_thread.setDaemon(True)
                run_thread.start()
                # 下载进程
                run_thread = threading.Thread(target=down_driver, args=[])
                run_thread.setDaemon(True)
                run_thread.start()
                # loading动画进程
                def loading():
                    Fun.SetElementVisible(uiName,"Progress_3",True)
                    for i in range(0,80,1):
                        Fun.SetCurrentValue(uiName,"Progress_3",i)
                        time.sleep(0.05)
                    for i in range(80,91,1):
                        Fun.SetCurrentValue(uiName,"Progress_3",i)
                        time.sleep(0.2)
                run_thread = threading.Thread(target=loading, args=[])
                run_thread.setDaemon(True)
                run_thread.start()

                
                
            except Exception as e:
                Fun.SetElementVisible(uiName,"Progress_3",False)
                Fun.SetElementVisible(uiName,"下载最新",True)
                Fun.MessageBox(text='下载失败，请重试！',title='错误',type='error',parent=None)
                print(e)
    else :
        print(ask)
        pass
        






















def 路径_onTextChanged(uiName,widgetName,text):
    pass






















