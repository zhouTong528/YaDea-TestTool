#coding=utf-8
#import libs 
import sys
import SAP_ALL_cmd
import SAP_ALL_sty
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
class  SAP_ALL:
    def __init__(self,root,isTKroot = True):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UICommandDictionary[uiName]=SAP_ALL_cmd
        Fun.Register(uiName,'root',root)
        style = SAP_ALL_sty.SetupStyle()
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
        Label_45 = tkinter.Label(Frame_17,text="Label")
        Fun.Register(uiName,'Label_45',Label_45,'雅迪图标')
        Fun.SetControlPlace(uiName,'Label_45',738,11,127,102)
        Label_45.configure(bg = "SystemButtonFace")
        Label_45.configure(fg = "SystemButtonText")
        SAP_ALL_cmd.ElementBGArray[45]=Fun.LoadImageFromFile("Resources/雅迪.png",None,uiName,'雅迪图标')
        SAP_ALL_cmd.ElementBGArray_Resize[45] = SAP_ALL_cmd.ElementBGArray[45].resize((127, 102),Image.LANCZOS)
        SAP_ALL_cmd.ElementBGArray_IM[45] = ImageTk.PhotoImage(SAP_ALL_cmd.ElementBGArray_Resize[45])
        Label_45.configure(image = SAP_ALL_cmd.ElementBGArray_IM[45])
        Label_45.configure(relief = "flat")
        Label_50 = tkinter.Label(Frame_17,text="整车收货入库")
        Fun.Register(uiName,'Label_50',Label_50,'Label_3')
        Fun.SetControlPlace(uiName,'Label_50',35,49,146,25)
        Label_50.configure(bg = "#FFFFFF")
        Label_50.configure(fg = "SystemButtonText")
        Label_50.configure(relief = "flat")
        Label_50_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_50.configure(font = Label_50_Ft)
        Label_51 = tkinter.Label(Frame_17,text="推送采购订单，固定商品！")
        Fun.Register(uiName,'Label_51',Label_51,'Label_4')
        Fun.SetControlPlace(uiName,'Label_51',184,41,219,48)#lock
        Label_51.configure(bg = "#FFFFFF")
        Label_51.configure(fg = "#CACACA")
        Label_51.configure(relief = "flat")
        Label_51_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='italic',underline=0,overstrike=0)
        Label_51.configure(font = Label_51_Ft)
        Label_52 = tkinter.Label(Frame_17,text="")
        Fun.Register(uiName,'Label_52',Label_52,'头秃')
        Fun.SetControlPlace(uiName,'Label_52',320,245,222,197)#lock
        Label_52.configure(bg = "SystemButtonFace")
        Label_52.configure(fg = "SystemButtonText")
        SAP_ALL_cmd.ElementBGArray[52]=Fun.LoadImageFromFile("Resources/头秃.png",None,uiName,'头秃')
        SAP_ALL_cmd.ElementBGArray_Resize[52] = SAP_ALL_cmd.ElementBGArray[52].resize((222, 197),Image.LANCZOS)
        SAP_ALL_cmd.ElementBGArray_IM[52] = ImageTk.PhotoImage(SAP_ALL_cmd.ElementBGArray_Resize[52])
        Label_52.configure(image = SAP_ALL_cmd.ElementBGArray_IM[52])
        Label_52.configure(relief = "flat")
        Label_53 = tkinter.Label(Frame_17,text="想不出来如何设计UI界面，请直接点击按钮")
        Fun.Register(uiName,'Label_53',Label_53,'文字')
        Fun.SetControlPlace(uiName,'Label_53',191,171,494,48)#lock
        Label_53.configure(bg = "#FFFFFF")
        Label_53.configure(fg = "SystemButtonText")
        Label_53.configure(relief = "flat")
        Label_53_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_53.configure(font = Label_53_Ft)
        Label_54 = tkinter.Label(Frame_17,text="")
        Fun.Register(uiName,'Label_54',Label_54,'Label_6')
        Fun.SetControlPlace(uiName,'Label_54',319,442,219,48)#lock
        Label_54.configure(bg = "#FFFFFF")
        Label_54.configure(fg = "SystemButtonText")
        Label_54.configure(relief = "flat")
        Label_54_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_54.configure(font = Label_54_Ft)
        LabelButton_46= EXUIControl.LabelButton(Frame_17)
        Fun.Register(uiName,'LabelButton_46',LabelButton_46,'整车单')
        LabelButton_46.SetText("推送SAP整车单")
        LabelButton_46.SetBGColor("#FFFFFF")
        LabelButton_46.SetFGColor("#FFFFFF")
        LabelButton_46_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_46.SetFont(LabelButton_46_TitleFont)
        LabelButton_46.SetBGImage("橙色按钮.png")
        LabelButton_46.SetBGColor_Hover("#FFFFFF")
        LabelButton_46.SetFGColor_Hover("#FFFFFF")
        LabelButton_46.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_46.SetBGColor_Click("#FFFFFF")
        LabelButton_46.SetFGColor_Click("#FFFFFF")
        LabelButton_46.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_46',538,520,200,48)#lock
        LabelButton_46.SetCommandFunction(SAP_ALL_cmd.整车单_onCommand,self.uiName,"整车单")
        LabelButton_48= EXUIControl.LabelButton(Frame_17)
        Fun.Register(uiName,'LabelButton_48',LabelButton_48,'随车单')
        LabelButton_48.SetText("推送SAP随车单")
        LabelButton_48.SetBGColor("#FFFFFF")
        LabelButton_48.SetFGColor("#FFFFFF")
        LabelButton_48_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_48.SetFont(LabelButton_48_TitleFont)
        LabelButton_48.SetBGImage("橙色按钮.png")
        LabelButton_48.SetBGColor_Hover("#FFFFFF")
        LabelButton_48.SetFGColor_Hover("#FFFFFF")
        LabelButton_48.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_48.SetBGColor_Click("#FFFFFF")
        LabelButton_48.SetFGColor_Click("#FFFFFF")
        LabelButton_48.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_48',257,520,200,48)#lock
        LabelButton_48.SetCommandFunction(SAP_ALL_cmd.随车单_onCommand,self.uiName,"随车单")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        SAP_ALL_cmd.Form_1_onLoad(uiName)
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
    MyDlg = SAP_ALL(root)
    root.mainloop()
