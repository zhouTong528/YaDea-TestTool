#coding=utf-8
import sys
import io
import os
import string
import math
import time
import base64
import tkinter
import tkinter.ttk
import tkinter.font
import tkinter.filedialog
import subprocess
import multiprocessing
import threading
import Fun
import API_cmd
import API_sty
import EXUIControl
import API
import main_cmd
import main_sty
import dianShang_win
import RTorder
import SAP_ALL
import SAP_PART
import api_store
import API_search
import chrome
import main
import chrome_cmd
import chrome_sty
import yaml
import json
import ast
import re
import numpy
import random
import response
import RTorder_cmd
import RTorder_sty
import SAP_ALL_cmd
import SAP_ALL_sty
import datetime
import traceback
import webbrowser
import Project1
import Project1_cmd
import Project1_sty
import win32api
import win32con
import win32gui_struct
import win32gui
import response_cmd
import response_sty
import SAP_PART_cmd
import SAP_PART_sty
import api_store_cmd
import api_store_sty
import API_search_cmd
import API_search_sty
import concurrent.futures
import chromedriver_autoinstaller
import winreg
import requests
import base64
import dianShang_win_cmd
import dianShang_win_sty
import Compile_Project1
#import libs 
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
from   tkinter import *
from   PIL import Image,ImageTk
from threading import Thread
MyDlg = None
import win32con
import win32gui
class SysTray(object):
    def __init__(self,uiName,icon,hover_text):
        self.uiName = uiName
        self.icon = icon
        self.hover_text = hover_text
        self.window_class_name = "SysTray"
        message_map = {win32gui.RegisterWindowMessage("TaskbarCreated"): self.refresh_icon,
                       win32con.WM_DESTROY: self.exit,
                       win32con.WM_USER+20 : self.notify,}
        window_class = win32gui.WNDCLASS()
        window_class.hInstance = win32gui.GetModuleHandle(None)
        window_class.lpszClassName = self.window_class_name
        window_class.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW 
        window_class.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
        window_class.hbrBackground = win32con.COLOR_WINDOW
        window_class.lpfnWndProc = message_map #也可以指定wndproc.
        self.classAtom = win32gui.RegisterClass(window_class)
    def build(self):
        hinst = win32gui.GetModuleHandle(None)
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = win32gui.CreateWindow(self.classAtom,
                                          self.window_class_name,
                                          style,
                                          0,
                                          0,
                                          win32con.CW_USEDEFAULT,
                                          win32con.CW_USEDEFAULT,
                                          0,
                                          0,
                                          hinst,
                                          None)
        win32gui.UpdateWindow(self.hwnd)
        self.notify_id = None
        self.refresh_icon()
        win32gui.PumpMessages()
    def exit(self):
        nid = (self.hwnd, 0)
        win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
        win32gui.PostQuitMessage(0) 
    def notify(self, hwnd, msg, wparam, lparam):
        if lparam == win32con.WM_RBUTTONUP:
            self.show_menu()
        elif lparam == win32con.WM_LBUTTONUP:
            self._handle = win32gui.FindWindow(None, '云销通实用组件V1.0.0           作者：Test-周通')
            win32gui.SendMessage(self._handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
            win32gui.SetForegroundWindow(self._handle)
        return True
    def refresh_icon(self, **data):
        hinst = win32gui.GetModuleHandle(None)
        if os.path.isfile(self.icon):
            icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            hicon = win32gui.LoadImage(hinst,
                                       self.icon,
                                       win32con.IMAGE_ICON,
                                       0,
                                       0,
                                       icon_flags)
        else:
            hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
        if self.notify_id: 
            message = win32gui.NIM_MODIFY
        else: 
            message = win32gui.NIM_ADD
        self.notify_id = (self.hwnd,
                          0,
                          win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP,
                          win32con.WM_USER+20,
                          hicon,
                          self.hover_text)
        win32gui.Shell_NotifyIcon(message, self.notify_id)
    def show_menu(self):
         #Create the Popup Menu
        global MyDlg
        SysTrayMenu = Menu(MyDlg.root,tearoff=0)
        SysTrayMenu.add_command(label="退出",command=lambda:Project1_cmd.tuichu("Project1","退出"))
        Pos = win32gui.GetCursorPos()
        SysTrayMenu.post(Pos[0],Pos[1])
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Project1:
    def __init__(self,root,isTKroot = True):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UICommandDictionary[uiName]=Project1_cmd
        Fun.Register(uiName,'root',root)
        style = Project1_sty.SetupStyle()
        if isTKroot == True:
            root.title("云销通实用组件V1.0.0           作者：Test-周通")
            Fun.WindowDraggable(root,False,0,'#FFFFFF')
            root.resizable(False,False)
            root.wm_attributes("-transparentcolor","#EC87C0")
            if os.path.exists("Resources/ico.png"):
                root.iconphoto(False, ImageTk.PhotoImage(file="Resources/ico.png"))
            Fun.CenterDlg(uiName,root,1209,785)
            root['background'] = '#FFFFFF'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 1209)
        Form_1.configure(height = 785)
        Form_1.configure(bg = "#EC87C0")
        Fun.SetRootRoundRectangle(Form_1,True,0,0,1209,785,radius=10,fill='#FFFFFF',outline='#FFFFFF',width=0)
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.SetCanvasBGImage(uiName,'Form_1',"Resources/login.png",'Original')
        Fun.G_RootSize=[1209,785]
        Group_1_Variable = Fun.AddTKVariable(uiName,'Group_1')
        Group_1_Variable.set(1)
        #Create the elements of root 
        LabelButton_4= EXUIControl.LabelButton(Form_1)
        Fun.Register(uiName,'LabelButton_4',LabelButton_4,'LabelButton_1')
        LabelButton_4.SetText("")
        LabelButton_4.SetBGColor("#FFFFFF")
        LabelButton_4.SetFGColor("#FFFFFF")
        LabelButton_4.SetBGImage("微信截图_20240117110808.png")
        LabelButton_4.SetBGColor_Hover("#FFFFFF")
        LabelButton_4.SetFGColor_Hover("#000000")
        LabelButton_4.SetBGImage_Hover("微信截图_20240117110808.png")
        LabelButton_4.SetBGColor_Click("#FFFFFF")
        LabelButton_4.SetFGColor_Click("#FF0000")
        LabelButton_4.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_4',560,583,216,66)
        LabelButton_4.SetCommandFunction(Project1_cmd.login_onCommand,self.uiName,"LabelButton_1")
        Label_7 = tkinter.Label(Form_1,text="雅迪云销通")
        Fun.Register(uiName,'Label_7',Label_7,'Label_1')
        Fun.SetControlPlace(uiName,'Label_7',543,113,318,61)
        Label_7.configure(bg = "#FFFFFF")
        Label_7.configure(fg = "SystemButtonText")
        Label_7.configure(anchor = "w")
        Label_7.configure(relief = "flat")
        Label_7_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=31,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_7.configure(font = Label_7_Ft)
        Label_11 = tkinter.Label(Form_1,text="登录账号")
        Fun.Register(uiName,'Label_11',Label_11,'Label_5')
        Fun.SetControlPlace(uiName,'Label_11',560,238,154,38)
        Label_11.configure(bg = "#FFFFFF")
        Label_11.configure(fg = "#656D78")
        Label_11.configure(anchor = "w")
        Label_11.configure(relief = "flat")
        Label_11_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=19,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_11.configure(font = Label_11_Ft)
        Label_12 = tkinter.Label(Form_1,text="密码")
        Fun.Register(uiName,'Label_12',Label_12,'Label_6')
        Fun.SetControlPlace(uiName,'Label_12',560,353,102,39)
        Label_12.configure(bg = "#FFFFFF")
        Label_12.configure(fg = "#656D78")
        Label_12.configure(anchor = "w")
        Label_12.configure(relief = "flat")
        Label_12_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=19,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_12.configure(font = Label_12_Ft)
        Label_17 = tkinter.Label(Form_1,text="Label")
        Fun.Register(uiName,'Label_17',Label_17,'Label_9')
        Fun.SetControlPlace(uiName,'Label_17',935,104,100,72)
        Label_17.configure(bg = "#EFEFEF")
        Label_17.configure(fg = "SystemButtonText")
        Project1_cmd.ElementBGArray[17]=Fun.LoadImageFromFile("Resources/Snipaste_2024-01-15_23-45-04.png",None,uiName,'Label_9')
        Project1_cmd.ElementBGArray_Resize[17] = Project1_cmd.ElementBGArray[17].resize((100, 72),Image.LANCZOS)
        Project1_cmd.ElementBGArray_IM[17] = ImageTk.PhotoImage(Project1_cmd.ElementBGArray_Resize[17])
        Label_17.configure(image = Project1_cmd.ElementBGArray_IM[17])
        Label_17.configure(relief = "flat")
        Label_21 = tkinter.Label(Form_1,text="欢迎使用！欢迎提供任何建议！                   作者：Test-周通")
        Fun.Register(uiName,'Label_21',Label_21,'Label_10')
        Fun.SetControlPlace(uiName,'Label_21',560,673,543,48)
        Label_21.configure(bg = "#FFFFFF")
        Label_21.configure(fg = "#AAB2BD")
        Label_21.configure(anchor = "w")
        Label_21.configure(relief = "flat")
        Label_21_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=10,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_21.configure(font = Label_21_Ft)
        Label_22 = tkinter.Label(Form_1,text="环境")
        Fun.Register(uiName,'Label_22',Label_22,'Label_11')
        Fun.SetControlPlace(uiName,'Label_22',560,459,102,39)
        Label_22.configure(bg = "#FFFFFF")
        Label_22.configure(fg = "#656D78")
        Label_22.configure(anchor = "w")
        Label_22.configure(relief = "flat")
        Label_22_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=19,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_22.configure(font = Label_22_Ft)
        Label_23 = tkinter.Label(Form_1,text="雅迪")
        Fun.Register(uiName,'Label_23',Label_23,'Label_12')
        Fun.SetControlPlace(uiName,'Label_23',1035,113,318,61)
        Label_23.configure(bg = "#FFFFFF")
        Label_23.configure(fg = "SystemButtonText")
        Label_23.configure(anchor = "w")
        Label_23.configure(relief = "flat")
        Label_23_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=31,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_23.configure(font = Label_23_Ft)
        Entry_20= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_20',Entry_20,'密码')
        Entry_20.SetBGColor("#FFFFFF")
        Entry_20.SetFGColor("#000000")
        Entry_20_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=15,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_20.SetFont(Entry_20_Font)
        Entry_20.SetShowChar("●")
        Entry_20.SetTipFGColor("#888888")
        Entry_20.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_20',560,402,549,48)
        Entry_20.bind("<Return>",Fun.EventFunction_Adaptor(Project1_cmd.密码_onKey_Return,uiName=uiName,widgetName="密码"))
        Entry_20.bind("<Key>",Fun.EventFunction_Adaptor(Project1_cmd.密码_onKey,uiName=uiName,widgetName="密码"))
        Entry_26= EXUIControl.CustomEntry(Form_1)
        Fun.Register(uiName,'Entry_26',Entry_26,'Entry_2')
        Entry_26.SetBGColor("#FFFFFF")
        Entry_26.SetFGColor("#000000")
        Entry_26_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=15,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_26.SetFont(Entry_26_Font)
        Entry_26.SetTipFGColor("#888888")
        Entry_26.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_26',560,292,549,48)
        ComboBox_25_Variable = Fun.AddTKVariable(uiName,'ComboBox_25')
        ComboBox_25 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_25_Variable, state="readonly")
        ComboBox_25_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=15,weight='normal',slant='roman',underline=0,overstrike=0)
        ComboBox_25.configure(font = ComboBox_25_Ft)
        Fun.Register(uiName,'ComboBox_25',ComboBox_25,'ComboBox_1')
        Fun.SetControlPlace(uiName,'ComboBox_25',560,511,320,48)
        ComboBox_25["values"]=['pre','uat','beta','prod']
        ComboBox_25.current(0)
        Fun.AddUserData(uiName,'ComboBox_25','env','string','',0)
        ComboBox_25.bind("<Return>",Fun.EventFunction_Adaptor(Project1_cmd.ComboBox_1_onKey_Return,uiName=uiName,widgetName="ComboBox_1"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Project1_cmd.Form_1_onLoad(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
        #Setup SysTray: (Keep This Line of comments)
        self.SetupSysTray()
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            self.root.bind('<Escape>',self.Escape)  
    def SetupSysTray(self):
        t = Thread(target=self.StartSysTrayThread, args=())
        t.setDaemon(True)
        t.start()
    def StartSysTrayThread(self):
        icons = r'Resources/ico.png'
        self.sysTray = SysTray(self.uiName,icons, "云销通实用组件V1.0.0           作者：Test-周通")
        Fun.Register(self.uiName,'SysTray',self.sysTray)
        self.sysTray.build()
    def GetRootSize(self):
        return Fun.G_RootSize[0],Fun.G_RootSize[1]
    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.uiName]
    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            self.Exit()
    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName)
            self.sysTray.exit()
    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.SetCanvasBGImage(self.uiName,'Form_1',"Resources/login.png",'Original')
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget:
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            uiName = self.uiName
            pass
        Fun.ActiveElement(self.uiName,event.widget)
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    root.withdraw()
    if Project1_cmd.Form_1_onInitCheck("Project1") == False:
        sys.exit()
    MyDlg = Project1(root)
    root.deiconify()
    root.mainloop()
