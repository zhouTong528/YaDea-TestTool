#coding=utf-8
#import libs 
import sys
import chrome_cmd
import chrome_sty
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
class  chrome:
    def __init__(self,root,isTKroot = True):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UICommandDictionary[uiName]=chrome_cmd
        Fun.Register(uiName,'root',root)
        style = chrome_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-transparentcolor","#00FFFF")
            Fun.CenterDlg(uiName,root,1188,687)
            root.wm_attributes("-topmost",1)
            root['background'] = '#F6F6F6'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
        Form_1.configure(width = 1188)
        Form_1.configure(height = 687)
        Form_1.configure(bg = "#F6F6F6")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[1188,687]
        #Create the elements of root 
        Frame_2 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'Frame_2',Frame_2,'Frame_1')
        Fun.SetControlPlace(uiName,'Frame_2',0,0,877,650)#lock
        Frame_2.configure(bg = "#FFFFFF")
        Frame_2.configure(relief = "flat")
        LabelFrame_3 = tkinter.LabelFrame(Frame_2,text="Version",takefocus = True,width = 10,height = 4)
        Fun.Register(uiName,'LabelFrame_3',LabelFrame_3,'LabelFrame_1')
        Fun.SetControlPlace(uiName,'LabelFrame_3',68,22,737,283)#lock
        LabelFrame_3.configure(bg = "#FFFFFF")
        LabelFrame_3.configure(fg = "SystemButtonText")
        LabelFrame_3.configure(relief = "groove")
        LabelFrame_3_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelFrame_3.configure(font = LabelFrame_3_Ft)
        Label_5 = tkinter.Label(Frame_2,text="本机目前的Chromedriver版本为：")
        Fun.Register(uiName,'Label_5',Label_5,'Label_2')
        Fun.SetControlPlace(uiName,'Label_5',85,152,438,48)#lock
        Label_5.configure(bg = "#FFFFFF")
        Label_5.configure(fg = "SystemButtonText")
        Label_5.configure(anchor = "w")
        Label_5.configure(relief = "flat")
        Label_5_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_5.configure(font = Label_5_Ft)
        Label_10 = tkinter.Label(Frame_2,text="本机目前的Chrome版本为：")
        Fun.Register(uiName,'Label_10',Label_10,'Label_3')
        Fun.SetControlPlace(uiName,'Label_10',85,84,438,48)#lock
        Label_10.configure(bg = "#FFFFFF")
        Label_10.configure(fg = "SystemButtonText")
        Label_10.configure(anchor = "w")
        Label_10.configure(relief = "flat")
        Label_10_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_10.configure(font = Label_10_Ft)
        Label_12 = tkinter.Label(Frame_2,text="")
        Fun.Register(uiName,'Label_12',Label_12,'Label_4')
        Fun.SetControlPlace(uiName,'Label_12',445,75,335,48)#lock
        Label_12.configure(bg = "#FFFFFF")
        Label_12.configure(fg = "SystemButtonText")
        Label_12.configure(relief = "flat")
        Label_12_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='bold',slant='italic',underline=1,overstrike=0)
        Label_12.configure(font = Label_12_Ft)
        Label_13 = tkinter.Label(Frame_2,text="")
        Fun.Register(uiName,'Label_13',Label_13,'driver')
        Fun.SetControlPlace(uiName,'Label_13',445,145,335,48)#lock
        Label_13.configure(bg = "#FFFFFF")
        Label_13.configure(fg = "#DA4453")
        Label_13.configure(relief = "flat")
        Label_13_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=18,weight='bold',slant='italic',underline=1,overstrike=0)
        Label_13.configure(font = Label_13_Ft)
        Label_16 = tkinter.Label(Frame_2,text="请选择下载目录：")
        Fun.Register(uiName,'Label_16',Label_16,'Label_5')
        Fun.SetControlPlace(uiName,'Label_16',30,320,200,48)#lock
        Label_16.configure(bg = "#FFFFFF")
        Label_16.configure(fg = "SystemButtonText")
        Label_16.configure(anchor = "w")
        Label_16.configure(relief = "flat")
        Label_16_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_16.configure(font = Label_16_Ft)
        Label_29 = tkinter.Label(Frame_2,text="Label")
        Fun.Register(uiName,'Label_29',Label_29,'Label_6')
        Fun.SetControlPlace(uiName,'Label_29',738,11,127,102)#lock
        Label_29.configure(bg = "SystemButtonFace")
        Label_29.configure(fg = "SystemButtonText")
        chrome_cmd.ElementBGArray[29]=Fun.LoadImageFromFile("Resources/雅迪.png",None,uiName,'Label_6')
        chrome_cmd.ElementBGArray_Resize[29] = chrome_cmd.ElementBGArray[29].resize((127, 102),Image.LANCZOS)
        chrome_cmd.ElementBGArray_IM[29] = ImageTk.PhotoImage(chrome_cmd.ElementBGArray_Resize[29])
        Label_29.configure(image = chrome_cmd.ElementBGArray_IM[29])
        Label_29.configure(relief = "flat")
        Label_29.lift()
        LabelButton_6= EXUIControl.LabelButton(Frame_2)
        Fun.Register(uiName,'LabelButton_6',LabelButton_6,'LabelButton_1')
        LabelButton_6.SetText("Chrome版本")
        LabelButton_6.SetBGColor("#FFFFFF")
        LabelButton_6.SetFGColor("#FFFFFF")
        LabelButton_6_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_6.SetFont(LabelButton_6_TitleFont)
        LabelButton_6.SetBGImage("橙色按钮.png")
        LabelButton_6.SetBGColor_Hover("#FFFFFF")
        LabelButton_6.SetFGColor_Hover("#FFFFFF")
        LabelButton_6.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_6.SetBGColor_Click("#FFFFFF")
        LabelButton_6.SetFGColor_Click("#FFFFFF")
        LabelButton_6.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_6',286,229,222,48)#lock
        LabelButton_6.SetCommandFunction(chrome_cmd.LabelButton_1_onCommand,self.uiName,"LabelButton_1")
        LabelButton_11= EXUIControl.LabelButton(Frame_2)
        Fun.Register(uiName,'LabelButton_11',LabelButton_11,'LabelButton_5')
        LabelButton_11.SetText("Chromedriver版本")
        LabelButton_11.SetBGColor("#FFFFFF")
        LabelButton_11.SetFGColor("#FFFFFF")
        LabelButton_11_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_11.SetFont(LabelButton_11_TitleFont)
        LabelButton_11.SetBGImage("橙色按钮.png")
        LabelButton_11.SetBGColor_Hover("#FFFFFF")
        LabelButton_11.SetFGColor_Hover("#FFFFFF")
        LabelButton_11.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_11.SetBGColor_Click("#FFFFFF")
        LabelButton_11.SetFGColor_Click("#FFFFFF")
        LabelButton_11.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_11',531,229,241,48)#lock
        LabelButton_11.SetCommandFunction(chrome_cmd.LabelButton_5_onCommand,self.uiName,"LabelButton_5")
        LabelButton_15= EXUIControl.LabelButton(Frame_2)
        Fun.Register(uiName,'LabelButton_15',LabelButton_15,'LabelButton_6')
        LabelButton_15.SetText("打开")
        LabelButton_15.SetBGColor("#FFFFFF")
        LabelButton_15.SetFGColor("#FFFFFF")
        LabelButton_15_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_15.SetFont(LabelButton_15_TitleFont)
        LabelButton_15.SetBGImage("橙色按钮.png")
        LabelButton_15.SetBGColor_Hover("#FFFFFF")
        LabelButton_15.SetFGColor_Hover("#FFFFFF")
        LabelButton_15.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_15.SetBGColor_Click("#FFFFFF")
        LabelButton_15.SetFGColor_Click("#FFFFFF")
        LabelButton_15.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_15',730,370,102,68)#lock
        LabelButton_15.SetCommandFunction(chrome_cmd.LabelButton_6_onCommand,self.uiName,"LabelButton_6")
        LabelButton_21= EXUIControl.LabelButton(Frame_2)
        Fun.Register(uiName,'LabelButton_21',LabelButton_21,'下载114前')
        LabelButton_21.SetText("下载114前Chromedriver")
        LabelButton_21.SetBGColor("#FFFFFF")
        LabelButton_21.SetFGColor("#FFFFFF")
        LabelButton_21_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_21.SetFont(LabelButton_21_TitleFont)
        LabelButton_21.SetBGImage("橙色按钮.png")
        LabelButton_21.SetBGColor_Hover("#FFFFFF")
        LabelButton_21.SetFGColor_Hover("#FFFFFF")
        LabelButton_21.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_21.SetBGColor_Click("#FFFFFF")
        LabelButton_21.SetFGColor_Click("#FFFFFF")
        LabelButton_21.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_21',115,484,280,48)#lock
        LabelButton_21.SetCommandFunction(chrome_cmd.下载114前_onCommand,self.uiName,"下载114前")
        LabelButton_24= EXUIControl.LabelButton(Frame_2)
        Fun.Register(uiName,'LabelButton_24',LabelButton_24,'下载最新')
        LabelButton_24.SetText("下载最新Chromedriver")
        LabelButton_24.SetBGColor("#FFFFFF")
        LabelButton_24.SetFGColor("#FFFFFF")
        LabelButton_24_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_24.SetFont(LabelButton_24_TitleFont)
        LabelButton_24.SetBGImage("橙色按钮.png")
        LabelButton_24.SetBGColor_Hover("#FFFFFF")
        LabelButton_24.SetFGColor_Hover("#FFFFFF")
        LabelButton_24.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_24.SetBGColor_Click("#FFFFFF")
        LabelButton_24.SetFGColor_Click("#FFFFFF")
        LabelButton_24.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_24',491,484,272,48)#lock
        LabelButton_24.SetCommandFunction(chrome_cmd.下载最新_onCommand,self.uiName,"下载最新")
        Entry_17= EXUIControl.CustomEntry(Frame_2)
        Fun.Register(uiName,'Entry_17',Entry_17,'路径')
        Entry_17.SetBGColor("#FFFFFF")
        Entry_17.SetFGColor("#000000")
        Entry_17.SetTipFGColor("#888888")
        Entry_17.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_17',120,380,571,48)#lock
        Entry_17.SetTextChangedFunction(chrome_cmd.路径_onTextChanged,uiName=uiName,widgetName="路径")
        Progress_27 = tkinter.ttk.Progressbar(Frame_2)
        Fun.Register(uiName,'Progress_27',Progress_27,'Progress_3')
        Fun.SetControlPlace(uiName,'Progress_27',495,495,262,26)#lock
        Progress_27.place_forget()
        Progress_27.configure(orient = tkinter.HORIZONTAL)
        Progress_27.configure(mode = "determinate")
        Progress_27.configure(maximum = "100")
        Progress_27.configure(value = "2")
        Progress_28 = tkinter.ttk.Progressbar(Frame_2)
        Fun.Register(uiName,'Progress_28',Progress_28,'114')
        Fun.SetControlPlace(uiName,'Progress_28',119,495,267,26)#lock
        Progress_28.place_forget()
        Progress_28.configure(orient = tkinter.HORIZONTAL)
        Progress_28.configure(mode = "determinate")
        Progress_28.configure(maximum = "100")
        Progress_28.configure(value = "0")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
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
    MyDlg = chrome(root)
    root.mainloop()
