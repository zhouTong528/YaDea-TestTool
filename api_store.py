#coding=utf-8
#import libs 
import sys
import api_store_cmd
import api_store_sty
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
class  api_store:
    def __init__(self,root,isTKroot = True):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UICommandDictionary[uiName]=api_store_cmd
        Fun.Register(uiName,'root',root)
        style = api_store_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-transparentcolor","#EC87C0")
            Fun.CenterDlg(uiName,root,1188,767)
            root.wm_attributes("-topmost",1)
            root['background'] = '#F6F6F6'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)#lock
        Form_1.configure(width = 1188)
        Form_1.configure(height = 767)
        Form_1.configure(bg = "#F6F6F6")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[1188,767]
        Group_1_Variable = Fun.AddTKVariable(uiName,'Group_1')
        Group_1_Variable.set(1)
        #Create the elements of root 
        Frame_17 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'Frame_17',Frame_17,'Frame_2')
        Fun.SetControlPlace(uiName,'Frame_17',0,0,877,650)#lock
        Frame_17.configure(bg = "#FFFFFF")
        Frame_17.configure(relief = "flat")
        Label_18 = tkinter.Label(Frame_17,text="门店编号")
        Fun.Register(uiName,'Label_18',Label_18,'Label_12')
        Fun.SetControlPlace(uiName,'Label_18',10,130,114,48)#lock
        Label_18.configure(bg = "#FFFFFF")
        Label_18.configure(fg = "SystemButtonText")
        Label_18.configure(relief = "flat")
        Label_18_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_18.configure(font = Label_18_Ft)
        Label_19 = tkinter.Label(Frame_17,text="门店级别")
        Fun.Register(uiName,'Label_19',Label_19,'Label_13')
        Fun.SetControlPlace(uiName,'Label_19',10,200,114,48)#lock
        Label_19.configure(bg = "#FFFFFF")
        Label_19.configure(fg = "SystemButtonText")
        Label_19.configure(relief = "flat")
        Label_19_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_19.configure(font = Label_19_Ft)
        Label_20 = tkinter.Label(Frame_17,text="门店状态")
        Fun.Register(uiName,'Label_20',Label_20,'Label_14')
        Fun.SetControlPlace(uiName,'Label_20',448,270,114,48)
        Label_20.configure(bg = "#FFFFFF")
        Label_20.configure(fg = "SystemButtonText")
        Label_20.configure(relief = "flat")
        Label_20_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_20.configure(font = Label_20_Ft)
        Label_21 = tkinter.Label(Frame_17,text="门店名称")
        Fun.Register(uiName,'Label_21',Label_21,'Label_15')
        Fun.SetControlPlace(uiName,'Label_21',448,130,114,48)
        Label_21.configure(bg = "#FFFFFF")
        Label_21.configure(fg = "SystemButtonText")
        Label_21.configure(relief = "flat")
        Label_21_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_21.configure(font = Label_21_Ft)
        Label_22 = tkinter.Label(Frame_17,text="是否总店")
        Fun.Register(uiName,'Label_22',Label_22,'Label_16')
        Fun.SetControlPlace(uiName,'Label_22',10,270,114,48)#lock
        Label_22.configure(bg = "#FFFFFF")
        Label_22.configure(fg = "SystemButtonText")
        Label_22.configure(relief = "flat")
        Label_22_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_22.configure(font = Label_22_Ft)
        Label_23 = tkinter.Label(Frame_17,text="门店类型")
        Fun.Register(uiName,'Label_23',Label_23,'Label_17')
        Fun.SetControlPlace(uiName,'Label_23',448,200,114,48)
        Label_23.configure(bg = "#FFFFFF")
        Label_23.configure(fg = "SystemButtonText")
        Label_23.configure(relief = "flat")
        Label_23_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_23.configure(font = Label_23_Ft)
        Label_43 = tkinter.Label(Frame_17,text="门店推送")
        Fun.Register(uiName,'Label_43',Label_43,'Label_18')
        Fun.SetControlPlace(uiName,'Label_43',10,38,167,48)
        Label_43.configure(bg = "#FFFFFF")
        Label_43.configure(fg = "SystemButtonText")
        Label_43.configure(relief = "flat")
        Label_43_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_43.configure(font = Label_43_Ft)
        Label_45 = tkinter.Label(Frame_17,text="Label")
        Fun.Register(uiName,'Label_45',Label_45,'Label_20')
        Fun.SetControlPlace(uiName,'Label_45',738,11,127,102)
        Label_45.configure(bg = "SystemButtonFace")
        Label_45.configure(fg = "SystemButtonText")
        api_store_cmd.ElementBGArray[45]=Fun.LoadImageFromFile("Resources/雅迪.png",None,uiName,'Label_20')
        api_store_cmd.ElementBGArray_Resize[45] = api_store_cmd.ElementBGArray[45].resize((127, 102),Image.LANCZOS)
        api_store_cmd.ElementBGArray_IM[45] = ImageTk.PhotoImage(api_store_cmd.ElementBGArray_Resize[45])
        Label_45.configure(image = api_store_cmd.ElementBGArray_IM[45])
        Label_45.configure(relief = "flat")
        Entry_26= EXUIControl.CustomEntry(Frame_17)
        Fun.Register(uiName,'Entry_26',Entry_26,'编码')
        Entry_26.SetBGColor("#FFFFFF")
        Entry_26.SetFGColor("#000000")
        Entry_26_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_26.SetFont(Entry_26_Font)
        Entry_26.SetTipFGColor("#888888")
        Entry_26.SetRelief("groove")
        Fun.SetControlPlace(uiName,'Entry_26',130,130,280,48)#lock
        Entry_26.bind("<Key>",Fun.EventFunction_Adaptor(api_store_cmd.Entry_3_onKey,uiName=uiName,widgetName="编码"))
        Entry_26.SetTextChangedFunction(api_store_cmd.编码_onTextChanged,uiName=uiName,widgetName="编码")
        Entry_27= EXUIControl.CustomEntry(Frame_17)
        Fun.Register(uiName,'Entry_27',Entry_27,'名称')
        Entry_27.SetBGColor("#FFFFFF")
        Entry_27.SetFGColor("#000000")
        Entry_27_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_27.SetFont(Entry_27_Font)
        Entry_27.SetTipFGColor("#888888")
        Entry_27.SetRelief("groove")
        Fun.SetControlPlace(uiName,'Entry_27',562,130,280,48)#lock
        Entry_27.bind("<Key>",Fun.EventFunction_Adaptor(api_store_cmd.Entry_4_onKey,uiName=uiName,widgetName="名称"))
        Entry_27.SetTextChangedFunction(api_store_cmd.名称_onTextChanged,uiName=uiName,widgetName="名称")
        ComboBox_38_Variable = Fun.AddTKVariable(uiName,'ComboBox_38')
        ComboBox_38 = tkinter.ttk.Combobox(Frame_17,textvariable=ComboBox_38_Variable, state="readonly")
        ComboBox_38_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        ComboBox_38.configure(font = ComboBox_38_Ft)
        Fun.Register(uiName,'ComboBox_38',ComboBox_38,'级别')
        Fun.SetControlPlace(uiName,'ComboBox_38',130,200,280,48)#lock
        ComboBox_38["values"]=['一网','二网']
        ComboBox_38.current(0)
        ComboBox_38.bind("<<ComboboxSelected>>",Fun.EventFunction_Adaptor(api_store_cmd.ComboBox_10_onSelect,uiName=uiName,widgetName="级别"))
        ComboBox_39_Variable = Fun.AddTKVariable(uiName,'ComboBox_39')
        ComboBox_39 = tkinter.ttk.Combobox(Frame_17,textvariable=ComboBox_39_Variable, state="readonly")
        ComboBox_39_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        ComboBox_39.configure(font = ComboBox_39_Ft)
        Fun.Register(uiName,'ComboBox_39',ComboBox_39,'是否总店')
        Fun.SetControlPlace(uiName,'ComboBox_39',130,270,280,48)#lock
        ComboBox_39["values"]=['否','是']
        ComboBox_39.current(0)
        ComboBox_39.lift()
        ComboBox_40_Variable = Fun.AddTKVariable(uiName,'ComboBox_40')
        ComboBox_40 = tkinter.ttk.Combobox(Frame_17,textvariable=ComboBox_40_Variable, state="readonly")
        ComboBox_40_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        ComboBox_40.configure(font = ComboBox_40_Ft)
        Fun.Register(uiName,'ComboBox_40',ComboBox_40,'类型')
        Fun.SetControlPlace(uiName,'ComboBox_40',562,200,280,48)#lock
        ComboBox_40["values"]=['销售店','综合店','服务站','服务体验中心','雅迪销售店','雅迪综合店']
        ComboBox_40.current(0)
        ComboBox_41_Variable = Fun.AddTKVariable(uiName,'ComboBox_41')
        ComboBox_41 = tkinter.ttk.Combobox(Frame_17,textvariable=ComboBox_41_Variable, state="readonly")
        ComboBox_41_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        ComboBox_41.configure(font = ComboBox_41_Ft)
        Fun.Register(uiName,'ComboBox_41',ComboBox_41,'状态')
        Fun.SetControlPlace(uiName,'ComboBox_41',562,270,280,48)#lock
        ComboBox_41["values"]=['启用','禁用']
        ComboBox_41.current(0)
        LabelButton_42= EXUIControl.LabelButton(Frame_17)
        Fun.Register(uiName,'LabelButton_42',LabelButton_42,'LabelButton_3')
        LabelButton_42.SetText("提交")
        LabelButton_42.SetBGColor("#FFFFFF")
        LabelButton_42.SetFGColor("#FFFFFF")
        LabelButton_42_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_42.SetFont(LabelButton_42_TitleFont)
        LabelButton_42.SetBGImage("橙色按钮.png")
        LabelButton_42.SetBGColor_Hover("#FFFFFF")
        LabelButton_42.SetFGColor_Hover("#FFFFFF")
        LabelButton_42.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_42.SetBGColor_Click("#FFFFFF")
        LabelButton_42.SetFGColor_Click("#FFFFFF")
        LabelButton_42.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_42',693,530,124,48)
        LabelButton_42.SetCommandFunction(api_store_cmd.LabelButton_3_onCommand,self.uiName,"LabelButton_3")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        api_store_cmd.Form_1_onLoad(uiName)
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
            pass
        Fun.ActiveElement(self.uiName,event.widget)
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = api_store(root)
    root.mainloop()
