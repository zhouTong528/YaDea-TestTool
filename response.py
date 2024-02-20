#coding=utf-8
#import libs 
import sys
import response_cmd
import response_sty
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
class  response:
    def __init__(self,root,isTKroot = True):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UICommandDictionary[uiName]=response_cmd
        Fun.Register(uiName,'root',root)
        style = response_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-transparentcolor","#EC87C0")
            Fun.CenterDlg(uiName,root,1117,767)
            root.wm_attributes("-topmost",1)
            root['background'] = '#F6F6F6'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 1117)
        Form_1.configure(height = 767)
        Form_1.configure(bg = "#F6F6F6")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[1117,767]
        Group_1_Variable = Fun.AddTKVariable(uiName,'Group_1')
        Group_1_Variable.set(1)
        #Create the elements of root 
        Frame_17 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'Frame_17',Frame_17,'Frame_2')
        Fun.SetControlPlace(uiName,'Frame_17',0,0,1.0,1.0)#lock
        Frame_17.configure(bg = "#FFFFFF")
        Frame_17.configure(relief = "flat")
        Label_45 = tkinter.Label(Frame_17,text="Label")
        Fun.Register(uiName,'Label_45',Label_45,'雅迪图标')
        Fun.SetControlPlace(uiName,'Label_45',961,14,127,102)#lock
        Label_45.configure(bg = "SystemButtonFace")
        Label_45.configure(fg = "SystemButtonText")
        response_cmd.ElementBGArray[45]=Fun.LoadImageFromFile("Resources/雅迪.png",None,uiName,'雅迪图标')
        response_cmd.ElementBGArray_Resize[45] = response_cmd.ElementBGArray[45].resize((127, 102),Image.LANCZOS)
        response_cmd.ElementBGArray_IM[45] = ImageTk.PhotoImage(response_cmd.ElementBGArray_Resize[45])
        Label_45.configure(image = response_cmd.ElementBGArray_IM[45])
        Label_45.configure(relief = "flat")
        Label_47 = tkinter.Label(Frame_17,text="响应码：")
        Fun.Register(uiName,'Label_47',Label_47,'Label_2')
        Fun.SetControlPlace(uiName,'Label_47',22,50,122,35)#lock
        Label_47.configure(bg = "#FFFFFF")
        Label_47.configure(fg = "SystemButtonText")
        Label_47.configure(relief = "flat")
        Label_47_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=15,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_47.configure(font = Label_47_Ft)
        Label_48 = tkinter.Label(Frame_17,text="")
        Fun.Register(uiName,'Label_48',Label_48,'Label_3')
        Fun.SetControlPlace(uiName,'Label_48',131,43,117,48)#lock
        Label_48.configure(bg = "#FFFFFF")
        Label_48.configure(fg = "SystemButtonText")
        Label_48.configure(anchor = "w")
        Label_48.configure(relief = "flat")
        Label_48_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=20,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_48.configure(font = Label_48_Ft)
        Text_46 = tkinter.Text(Frame_17,undo=True,wrap=WORD)
        Fun.Register(uiName,'Text_46',Text_46,'Text_1')
        Fun.SetControlPlace(uiName,'Text_46',22,121,1078,635)
        Text_46.configure(bg = "#FFFFFF")
        Text_46.configure(fg = "SystemWindowText")
        Text_46.configure(relief = "sunken")
        Text_46_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Text_46.configure(font = Text_46_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        response_cmd.Form_1_onLoad(uiName)
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
    MyDlg = response(root)
    root.mainloop()
