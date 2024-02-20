#coding=utf-8
#import libs 
import sys
import API_search_cmd
import API_search_sty
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
class  API_search:
    def __init__(self,root,isTKroot = True):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UICommandDictionary[uiName]=API_search_cmd
        Fun.Register(uiName,'root',root)
        style = API_search_sty.SetupStyle()
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
        API_search_cmd.ElementBGArray[45]=Fun.LoadImageFromFile("Resources/雅迪.png",None,uiName,'雅迪图标')
        API_search_cmd.ElementBGArray_Resize[45] = API_search_cmd.ElementBGArray[45].resize((127, 102),Image.LANCZOS)
        API_search_cmd.ElementBGArray_IM[45] = ImageTk.PhotoImage(API_search_cmd.ElementBGArray_Resize[45])
        Label_45.configure(image = API_search_cmd.ElementBGArray_IM[45])
        Label_45.configure(relief = "flat")
        Label_48 = tkinter.Label(Frame_17,text="API接口查询")
        Fun.Register(uiName,'Label_48',Label_48,'Label_2')
        Fun.SetControlPlace(uiName,'Label_48',11,38,200,48)
        Label_48.configure(bg = "#FFFFFF")
        Label_48.configure(fg = "SystemButtonText")
        Label_48.configure(anchor = "w")
        Label_48.configure(relief = "flat")
        Label_48_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=20,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_48.configure(font = Label_48_Ft)
        ListView_46 = tkinter.ttk.Treeview(Frame_17,show="headings")
        Fun.Register(uiName,'ListView_46',ListView_46,'ListView_1')
        Fun.SetControlPlace(uiName,'ListView_46',37,124,803,401)#lock
        ListView_46.configure(selectmode = "extended")
        style.configure("ListView_46.Treeview.Heading",font=('微软雅黑', 12))
        ListView_46.config(style="ListView_46.Treeview")
        ListView_46.configure(columns = ["序号","接口名称","API地址","请求方式"])
        ListView_46.column("序号",anchor="center",width=50,stretch=True)
        ListView_46.heading("序号",anchor="center",text="序号")
        ListView_46.column("接口名称",anchor="center",width=180,stretch=True)
        ListView_46.heading("接口名称",anchor="center",text="接口名称")
        ListView_46.column("API地址",anchor="center",width=300,stretch=True)
        ListView_46.heading("API地址",anchor="center",text="API地址")
        ListView_46.column("请求方式",anchor="center",width=80,stretch=True)
        ListView_46.heading("请求方式",anchor="center",text="请求方式")
        ListView_46_VScrollbar = tkinter.ttk.Scrollbar(ListView_46,orient=tkinter.VERTICAL)
        ListView_46_VScrollbar.place(x = 783,y = 0,width = 20,height = 401)
        ListView_46_VScrollbar.config(command = ListView_46.yview)
        ListView_46.config(yscrollcommand = ListView_46_VScrollbar.set)
        Fun.Register(uiName,'ListView_46_VScrollbar',ListView_46_VScrollbar)
        LabelButton_47= EXUIControl.LabelButton(Frame_17)
        Fun.Register(uiName,'LabelButton_47',LabelButton_47,'LabelButton_1')
        LabelButton_47.SetText("删除")
        LabelButton_47.SetBGColor("#FFFFFF")
        LabelButton_47.SetFGColor("#FFFFFF")
        LabelButton_47_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_47.SetFont(LabelButton_47_TitleFont)
        LabelButton_47.SetBGImage("橙色按钮.png")
        LabelButton_47.SetBGColor_Hover("#FFFFFF")
        LabelButton_47.SetFGColor_Hover("#FFFFFF")
        LabelButton_47.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_47.SetBGColor_Click("#FFFFFF")
        LabelButton_47.SetFGColor_Click("#FFFFFF")
        LabelButton_47.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_47',687,554,107,48)#lock
        LabelButton_47.SetCommandFunction(API_search_cmd.LabelButton_1_onCommand,self.uiName,"LabelButton_1")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        API_search_cmd.Form_1_onLoad(uiName)
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
    MyDlg = API_search(root)
    root.mainloop()
