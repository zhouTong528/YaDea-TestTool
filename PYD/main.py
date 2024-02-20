#coding=utf-8
#import libs 
import sys
import main_cmd
import main_sty
import Fun
import EXUIControl
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  main:
    def __init__(self,root,isTKroot = True):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UICommandDictionary[uiName]=main_cmd
        Fun.Register(uiName,'root',root)
        style = main_sty.SetupStyle()
        if isTKroot == True:
            root.title("云销通实用组件V1.0.0           作者：Test-周通")
            Fun.WindowDraggable(root,True,0,'#FFFFFF')
            root.wm_attributes("-transparentcolor","#00FFFF")
            Fun.CenterDlg(uiName,root,1188,783)
            root['background'] = '#F6F6F6'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 1188)
        Form_1.configure(height = 783)
        Form_1.configure(bg = "#F6F6F6")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[1188,783]
        #Create the elements of root 
        Frame_2 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'Frame_2',Frame_2,'Frame_1')
        Fun.SetControlPlace(uiName,'Frame_2',-30,0,1224,57)#lock
        Frame_2.configure(bg = "#FF7816")
        Frame_2.configure(relief = "flat")
        Button_3 = tkinter.Button(Frame_2,text="访问云销通")
        Fun.Register(uiName,'Button_3',Button_3,'Button_1')
        Fun.SetControlPlace(uiName,'Button_3',1078,0,140,57)#lock
        Button_3.configure(bg = "#FFFFFF")
        Button_3.configure(command=lambda:main_cmd.Button_1_onCommand(uiName,"Button_1"))
        Button_3_Ft=tkinter.font.Font(family='Microsoft YaHei UI Light', size=10,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_3.configure(font = Button_3_Ft)
        Button_11 = tkinter.Button(Frame_2,text="切换账号")
        Fun.Register(uiName,'Button_11',Button_11,'切换账号')
        Fun.SetControlPlace(uiName,'Button_11',29,0,140,57)#lock
        Button_11.configure(bg = "#FFFFFF")
        Button_11.configure(command=lambda:main_cmd.切换账号_onCommand(uiName,"切换账号"))
        Button_11_Ft=tkinter.font.Font(family='Microsoft YaHei UI Light', size=10,weight='normal',slant='roman',underline=0,overstrike=0)
        Button_11.configure(font = Button_11_Ft)
        Label_9 = tkinter.Label(Frame_2,text="")
        Fun.Register(uiName,'Label_9',Label_9,'env显示')
        Fun.SetControlPlace(uiName,'Label_9',1003,0,75,57)#lock
        Label_9.configure(bg = "#FF7816")
        Label_9.configure(fg = "#FFFFFF")
        Label_9.configure(relief = "flat")
        Label_9_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=15,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_9.configure(font = Label_9_Ft)
        Label_14 = tkinter.Label(Frame_2,text="当前门店")
        Fun.Register(uiName,'Label_14',Label_14,'当前门店')
        Fun.SetControlPlace(uiName,'Label_14',403,0,119,57)#lock
        Label_14.configure(bg = "#FFFFFF")
        Label_14.configure(fg = "SystemButtonText")
        Label_14.configure(relief = "flat")
        Label_14_Ft=tkinter.font.Font(family='新宋体', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_14.configure(font = Label_14_Ft)
        ComboBox_13_Variable = Fun.AddTKVariable(uiName,'ComboBox_13')
        ComboBox_13 = tkinter.ttk.Combobox(Frame_2,textvariable=ComboBox_13_Variable, state="readonly")
        ComboBox_13_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        ComboBox_13.configure(font = ComboBox_13_Ft)
        Fun.Register(uiName,'ComboBox_13',ComboBox_13,'门店下拉框')
        Fun.SetControlPlace(uiName,'ComboBox_13',522,0,300,57)#lock
        ComboBox_13.bind("<<ComboboxSelected>>",Fun.EventFunction_Adaptor(main_cmd.门店下拉框_onSelect,uiName=uiName,widgetName="门店下拉框"))
        Frame_17 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'Frame_17',Frame_17,'Frame_2')
        Fun.SetControlPlace(uiName,'Frame_17',300,80,877,675)#lock
        Frame_17.configure(bg = "#FFFFFF")
        Frame_17.configure(relief = "flat")
        Label_28 = tkinter.Label(Frame_17,text="La\r")
        Fun.Register(uiName,'Label_28',Label_28,'Label_5')
        Fun.SetControlPlace(uiName,'Label_28',738,11,127,102)#lock
        Label_28.configure(bg = "SystemButtonFace")
        Label_28.configure(fg = "SystemButtonText")
        main_cmd.ElementBGArray[28]=Fun.LoadImageFromFile("Resources/雅迪.png",None,uiName,'Label_5')
        main_cmd.ElementBGArray_Resize[28] = main_cmd.ElementBGArray[28].resize((127, 102),Image.LANCZOS)
        main_cmd.ElementBGArray_IM[28] = ImageTk.PhotoImage(main_cmd.ElementBGArray_Resize[28])
        Label_28.configure(image = main_cmd.ElementBGArray_IM[28])
        Label_28.configure(relief = "flat")
        Label_32 = tkinter.Label(Frame_17,text="登录账号")
        Fun.Register(uiName,'Label_32',Label_32,'账号')
        Fun.SetControlPlace(uiName,'Label_32',0,166,150,48)#lock
        Label_32.configure(bg = "#FFFFFF")
        Label_32.configure(fg = "SystemButtonText")
        Label_32.configure(relief = "flat")
        Label_32_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_32.configure(font = Label_32_Ft)
        Label_33 = tkinter.Label(Frame_17,text="账号名称")
        Fun.Register(uiName,'Label_33',Label_33,'名称')
        Fun.SetControlPlace(uiName,'Label_33',0,214,150,48)#lock
        Label_33.configure(bg = "#FFFFFF")
        Label_33.configure(fg = "SystemButtonText")
        Label_33.configure(relief = "flat")
        Label_33_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_33.configure(font = Label_33_Ft)
        Label_34 = tkinter.Label(Frame_17,text="角色权限")
        Fun.Register(uiName,'Label_34',Label_34,'角色')
        Fun.SetControlPlace(uiName,'Label_34',0,262,150,48)#lock
        Label_34.configure(bg = "#FFFFFF")
        Label_34.configure(fg = "SystemButtonText")
        Label_34.configure(relief = "flat")
        Label_34_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_34.configure(font = Label_34_Ft)
        Label_36 = tkinter.Label(Frame_17,text="")
        Fun.Register(uiName,'Label_36',Label_36,'acc')
        Fun.SetControlPlace(uiName,'Label_36',150,166,200,48)#lock
        Label_36.configure(bg = "#FFFFFF")
        Label_36.configure(fg = "SystemButtonText")
        Label_36.configure(anchor = "w")
        Label_36.configure(relief = "flat")
        Label_36_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_36.configure(font = Label_36_Ft)
        Label_37 = tkinter.Label(Frame_17,text="")
        Fun.Register(uiName,'Label_37',Label_37,'name')
        Fun.SetControlPlace(uiName,'Label_37',150,214,363,48)#lock
        Label_37.configure(bg = "#FFFFFF")
        Label_37.configure(fg = "SystemButtonText")
        Label_37.configure(anchor = "w")
        Label_37.configure(relief = "flat")
        Label_37_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_37.configure(font = Label_37_Ft)
        Label_38 = tkinter.Label(Frame_17,text="")
        Fun.Register(uiName,'Label_38',Label_38,'Label_9')
        Fun.SetControlPlace(uiName,'Label_38',150,262,200,48)#lock
        Label_38.configure(bg = "#FFFFFF")
        Label_38.configure(fg = "SystemButtonText")
        Label_38.configure(anchor = "w")
        Label_38.configure(relief = "flat")
        Label_38_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_38.configure(font = Label_38_Ft)
        Label_39 = tkinter.Label(Frame_17,text="租户ID")
        Fun.Register(uiName,'Label_39',Label_39,'Label_10')
        Fun.SetControlPlace(uiName,'Label_39',0,310,150,48)#lock
        Label_39.configure(bg = "#FFFFFF")
        Label_39.configure(fg = "SystemButtonText")
        Label_39.configure(relief = "flat")
        Label_39_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_39.configure(font = Label_39_Ft)
        Label_40 = tkinter.Label(Frame_17,text="")
        Fun.Register(uiName,'Label_40',Label_40,'Label_11')
        Fun.SetControlPlace(uiName,'Label_40',150,310,200,48)#lock
        Label_40.configure(bg = "#FFFFFF")
        Label_40.configure(fg = "SystemButtonText")
        Label_40.configure(anchor = "w")
        Label_40.configure(relief = "flat")
        Label_40_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_40.configure(font = Label_40_Ft)
        Label_41 = tkinter.Label(Frame_17,text="")
        Fun.Register(uiName,'Label_41',Label_41,'Label_12')
        Fun.SetControlPlace(uiName,'Label_41',462,337,328,241)
        Label_41.configure(bg = "SystemButtonFace")
        Label_41.configure(fg = "SystemButtonText")
        main_cmd.ElementBGArray[41]=Fun.LoadImageFromFile("Resources/表情包.png",None,uiName,'Label_12')
        main_cmd.ElementBGArray_Resize[41] = main_cmd.ElementBGArray[41].resize((328, 241),Image.LANCZOS)
        main_cmd.ElementBGArray_IM[41] = ImageTk.PhotoImage(main_cmd.ElementBGArray_Resize[41])
        Label_41.configure(image = main_cmd.ElementBGArray_IM[41])
        Label_41.configure(relief = "flat")
        Label_42 = tkinter.Label(Frame_17,text="加载成功！一切OK")
        Fun.Register(uiName,'Label_42',Label_42,'Label_13')
        Fun.SetControlPlace(uiName,'Label_42',451,289,323,48)
        Label_42.configure(bg = "#FFFFFF")
        Label_42.configure(fg = "SystemButtonText")
        Label_42.configure(relief = "flat")
        Label_42_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_42.configure(font = Label_42_Ft)
        ListMenu_16= EXUIControl.ListMenu(Form_1)
        Fun.Register(uiName,'ListMenu_16',ListMenu_16,'导航栏')
        ListMenu_16.SetBGColor("#FFFFFF")
        ListMenu_16.SetTitleAnchor('left')
        ListMenu_16.SetTitleCompound('left')
        ListMenu_16.SetTitleSpacingX(10)
        ListMenu_16.SetTitleSpacingY(0)
        ListMenu_16.SetTitleBGColor("#FFFFFF")
        ListMenu_16.SetTitleFGColor("#000000")
        ListMenu_16_TitleFont=tkinter.font.Font(family='新宋体', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        ListMenu_16.SetTitleFont(ListMenu_16_TitleFont)
        ListMenu_16.SetTitleBGColor_Hover("#FFFFFF")
        ListMenu_16.SetTitleFGColor_Hover("#000000")
        ListMenu_16_TitleFont_Hover=tkinter.font.Font(family='新宋体', size=13,weight='bold',slant='roman',underline=0,overstrike=0)
        ListMenu_16.SetTitleFont_Hover(ListMenu_16_TitleFont_Hover)
        ListMenu_16.SetTitleBGColor_Click("#FFFFFF")
        ListMenu_16.SetTitleFGColor_Click("#000000")
        ListMenu_16_TitleFont_Click=tkinter.font.Font(family='新宋体', size=12,weight='bold',slant='roman',underline=0,overstrike=0)
        ListMenu_16.SetTitleFont_Click(ListMenu_16_TitleFont_Click)
        ListMenu_16.SetItemAnchor('left')
        ListMenu_16.SetItemCompound('left')
        ListMenu_16.SetItemSpacingX(0)
        ListMenu_16.SetItemSpacingY(0)
        ListMenu_16.SetItemBGColor("#FFFFFF")
        ListMenu_16.SetItemFGColor("#000000")
        ListMenu_16_ItemFont=tkinter.font.Font(family='新宋体', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        ListMenu_16.SetItemFont(ListMenu_16_ItemFont)
        ListMenu_16.SetItemBGColor_Hover("#FFFFFF")
        ListMenu_16.SetItemFGColor_Hover("#FF7816")
        ListMenu_16_ItemFont_Hover=tkinter.font.Font(family='新宋体', size=15,weight='bold',slant='roman',underline=0,overstrike=0)
        ListMenu_16.SetItemFont_Hover(ListMenu_16_ItemFont_Hover)
        ListMenu_16.SetItemBGColor_Click("#FFEDDF")
        ListMenu_16.SetItemFGColor_Click("#FF7816")
        ListMenu_16_ItemFont_Click=tkinter.font.Font(family='Arial', size=14,weight='bold',slant='roman',underline=0,overstrike=0)
        ListMenu_16.SetItemFont_Click(ListMenu_16_ItemFont_Click)
        Fun.SetControlPlace(uiName,'ListMenu_16',29,80,250,661)
        ListMenu_16.AddTitle("零售管理","二网补贴配置 icon.png")
        ListMenu_16.AddItem("电商发货订单","零售管理","","dianShang_win.py")
        ListMenu_16.AddItem("电商退货订单","零售管理","","RTorder.py")
        ListMenu_16.AddTitle("批发管理","救援工单 icon.png")
        ListMenu_16.AddItem("API接口自动化 开发ing","批发管理")
        ListMenu_16.AddItem("WebUI自动化 开发ing","批发管理")
        ListMenu_16.AddTitle("采购管理","工单结算明细 icon.png")
        ListMenu_16.AddItem("SAP整车采购单","采购管理","","SAP_ALL.py")
        ListMenu_16.AddItem("SAP配件采购单","采购管理","","SAP_PART.py")
        ListMenu_16.AddTitle("系统设置","操作日志 icon.png")
        ListMenu_16.AddItem("门店推送","系统设置","","api_store.py")
        ListMenu_16.AddTitle("自动化配置","仓库设置 icon.png")
        ListMenu_16.AddItem("API接口请求","自动化配置","","API.py")
        ListMenu_16.AddItem("API接口查询","自动化配置","","API_search.py")
        ListMenu_16.AddItem("下载Chromedriver","自动化配置","","chrome.py")
        ListMenu_16.SetListMenuCallBackFunction(main_cmd.导航栏_onItemSelect,uiName,"导航栏")
        #Create the Menu of root 
        MainMenu=tkinter.Menu(root)
        root.config(menu = MainMenu)
        设置=tkinter.Menu(MainMenu,tearoff = 0)
        设置.add_command(label="检查",command=lambda:main_cmd.jiancha(uiName,"检查"))
        MainMenu.add_cascade(label="设置",menu=设置)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        main_cmd.Form_1_onLoad(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            self.root.bind('<Escape>',self.Escape)  
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

    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget:
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            uiName = self.uiName
            Fun.SetControlPlace(uiName,'Frame_1',-30,0,1224,57)#lock
            pass
        Fun.ActiveElement(self.uiName,event.widget)
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = main(root)
    root.mainloop()
