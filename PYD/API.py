#coding=utf-8
#import libs 
import sys
import API_cmd
import API_sty
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
class  API:
    def __init__(self,root,isTKroot = True):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UICommandDictionary[uiName]=API_cmd
        Fun.Register(uiName,'root',root)
        style = API_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.WindowDraggable(root,False,0,'#ffffff')
            root.wm_attributes("-transparentcolor","#EC87C0")
            Fun.CenterDlg(uiName,root,1188,762)
            root.wm_attributes("-topmost",1)
            root['background'] = '#F6F6F6'
        root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)#lock
        Form_1.configure(width = 1188)
        Form_1.configure(height = 762)
        Form_1.configure(bg = "#F6F6F6")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Fun.G_RootSize=[1188,762]
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
        API_cmd.ElementBGArray[45]=Fun.LoadImageFromFile("Resources/雅迪.png",None,uiName,'雅迪图标')
        API_cmd.ElementBGArray_Resize[45] = API_cmd.ElementBGArray[45].resize((127, 102),Image.LANCZOS)
        API_cmd.ElementBGArray_IM[45] = ImageTk.PhotoImage(API_cmd.ElementBGArray_Resize[45])
        Label_45.configure(image = API_cmd.ElementBGArray_IM[45])
        Label_45.configure(relief = "flat")
        Label_70 = tkinter.Label(Frame_17,text="接口模拟快速请求")
        Fun.Register(uiName,'Label_70',Label_70,'Label_2')
        Fun.SetControlPlace(uiName,'Label_70',5,0,226,48)#lock
        Label_70.configure(bg = "#FFFFFF")
        Label_70.configure(fg = "SystemButtonText")
        Label_70.configure(relief = "flat")
        Label_70_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=20,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_70.configure(font = Label_70_Ft)
        Label_73 = tkinter.Label(Frame_17,text="选择接口")
        Fun.Register(uiName,'Label_73',Label_73,'Label_3')
        Fun.SetControlPlace(uiName,'Label_73',5,551,99,48)#lock
        Label_73.configure(bg = "#FFFFFF")
        Label_73.configure(fg = "#000000")
        Label_73.configure(relief = "flat")
        Label_73_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=15,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_73.configure(font = Label_73_Ft)
        Label_77 = tkinter.Label(Frame_17,text="请注意填写的格式")
        Fun.Register(uiName,'Label_77',Label_77,'Label_4')
        Fun.SetControlPlace(uiName,'Label_77',587,156,147,24)#lock
        Label_77.configure(bg = "#FFFFFF")
        Label_77.configure(fg = "#656D78")
        Label_77.configure(anchor = "w")
        Label_77.configure(relief = "flat")
        Label_77_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_77.configure(font = Label_77_Ft)
        Label_78 = tkinter.Label(Frame_17,text="发送无响应,请检查填写的参数是否正确")
        Fun.Register(uiName,'Label_78',Label_78,'Label_5')
        Fun.SetControlPlace(uiName,'Label_78',587,180,290,26)#lock
        Label_78.configure(bg = "#FFFFFF")
        Label_78.configure(fg = "#656D78")
        Label_78.configure(anchor = "w")
        Label_78.configure(relief = "flat")
        Label_78_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_78.configure(font = Label_78_Ft)
        Label_79 = tkinter.Label(Frame_17,text="注意使用英文下的符号({},)")
        Fun.Register(uiName,'Label_79',Label_79,'Label_6')
        Fun.SetControlPlace(uiName,'Label_79',587,206,220,26)#lock
        Label_79.configure(bg = "#FFFFFF")
        Label_79.configure(fg = "#656D78")
        Label_79.configure(anchor = "w")
        Label_79.configure(relief = "flat")
        Label_79_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_79.configure(font = Label_79_Ft)
        LabelButton_46= EXUIControl.LabelButton(Frame_17)
        Fun.Register(uiName,'LabelButton_46',LabelButton_46,'发送')
        LabelButton_46.SetText("发送请求")
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
        Fun.SetControlPlace(uiName,'LabelButton_46',681,551,131,48)#lock
        LabelButton_46.SetCommandFunction(API_cmd.发送_onCommand,self.uiName,"发送")
        LabelButton_72= EXUIControl.LabelButton(Frame_17)
        Fun.Register(uiName,'LabelButton_72',LabelButton_72,'LabelButton_3')
        LabelButton_72.SetText("保存请求")
        LabelButton_72.SetBGColor("#FFFFFF")
        LabelButton_72.SetFGColor("#FFFFFF")
        LabelButton_72_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_72.SetFont(LabelButton_72_TitleFont)
        LabelButton_72.SetBGImage("橙色按钮.png")
        LabelButton_72.SetBGColor_Hover("#FFFFFF")
        LabelButton_72.SetFGColor_Hover("#FFFFFF")
        LabelButton_72.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_72.SetBGColor_Click("#FFFFFF")
        LabelButton_72.SetFGColor_Click("#FFFFFF")
        LabelButton_72.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_72',503,551,131,48)#lock
        LabelButton_72.SetCommandFunction(API_cmd.LabelButton_3_onCommand,self.uiName,"LabelButton_3")
        Entry_53= EXUIControl.CustomEntry(Frame_17)
        Fun.Register(uiName,'Entry_53',Entry_53,'Entry_2')
        Entry_53.SetBGColor("#FFFFFF")
        Entry_53.SetFGColor("#000000")
        Entry_53_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_53.SetFont(Entry_53_Font)
        Entry_53.SetTipFGColor("#888888")
        Entry_53.SetRelief("groove")
        Entry_53.SetState("readonly")
        Fun.SetControlPlace(uiName,'Entry_53',109,106,468,40)#lock
        Entry_54= EXUIControl.CustomEntry(Frame_17)
        Fun.Register(uiName,'Entry_54',Entry_54,'Entry_3')
        Entry_54.SetBGColor("#FFFFFF")
        Entry_54.SetFGColor("#000000")
        Entry_54_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_54.SetFont(Entry_54_Font)
        Entry_54.SetTipFGColor("#888888")
        Entry_54.SetRelief("groove")
        Fun.SetControlPlace(uiName,'Entry_54',109,210,468,40)#lock
        Entry_54.bind("<Key>",Fun.EventFunction_Adaptor(API_cmd.Entry_3_onKey,uiName=uiName,widgetName="Entry_3"))
        Entry_55= EXUIControl.CustomEntry(Frame_17)
        Fun.Register(uiName,'Entry_55',Entry_55,'Entry_4')
        Entry_55.SetText("Headers")
        Entry_55.SetBGColor("#CACACA")
        Entry_55.SetFGColor("#000000")
        Entry_55_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_55.SetFont(Entry_55_Font)
        Entry_55.SetJustify("center")
        Entry_55.SetTipFGColor("#888888")
        Entry_55.SetRelief("flat")
        Entry_55.SetRoundRadius(10)
        Entry_55.SetState("readonly")
        Fun.SetControlPlace(uiName,'Entry_55',20,210,89,40)#lock
        Entry_55.bind("<Key>",Fun.EventFunction_Adaptor(API_cmd.Entry_4_onKey,uiName=uiName,widgetName="Entry_4"))
        Entry_56= EXUIControl.CustomEntry(Frame_17)
        Fun.Register(uiName,'Entry_56',Entry_56,'Entry_5')
        Entry_56.SetText("Host")
        Entry_56.SetBGColor("#CACACA")
        Entry_56.SetFGColor("#000000")
        Entry_56_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_56.SetFont(Entry_56_Font)
        Entry_56.SetJustify("center")
        Entry_56.SetTipFGColor("#888888")
        Entry_56.SetRelief("flat")
        Entry_56.SetRoundRadius(10)
        Entry_56.SetState("readonly")
        Fun.SetControlPlace(uiName,'Entry_56',20,106,89,40)#lock
        Entry_59= EXUIControl.CustomEntry(Frame_17)
        Fun.Register(uiName,'Entry_59',Entry_59,'Entry_7')
        Entry_59.SetBGColor("#FFFFFF")
        Entry_59.SetFGColor("#000000")
        Entry_59_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_59.SetFont(Entry_59_Font)
        Entry_59.SetTipText("无需填写token，发送时会自动填写")
        Entry_59.SetTipFGColor("#888888")
        Entry_59.SetRelief("groove")
        Fun.SetControlPlace(uiName,'Entry_59',109,210,468,40)#lock
        Entry_60= EXUIControl.CustomEntry(Frame_17)
        Fun.Register(uiName,'Entry_60',Entry_60,'Entry_8')
        Entry_60.SetBGColor("#FFFFFF")
        Entry_60.SetFGColor("#000000")
        Entry_60_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_60.SetFont(Entry_60_Font)
        Entry_60.SetTipText("api地址")
        Entry_60.SetTipFGColor("#888888")
        Entry_60.SetRelief("groove")
        Fun.SetControlPlace(uiName,'Entry_60',110,159,468,40)#lock
        Entry_75= EXUIControl.CustomEntry(Frame_17)
        Fun.Register(uiName,'Entry_75',Entry_75,'Entry_9')
        Entry_75.SetText("名称")
        Entry_75.SetBGColor("#CACACA")
        Entry_75.SetFGColor("#000000")
        Entry_75_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=14,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_75.SetFont(Entry_75_Font)
        Entry_75.SetJustify("center")
        Entry_75.SetTipFGColor("#888888")
        Entry_75.SetRelief("flat")
        Entry_75.SetRoundRadius(10)
        Entry_75.SetState("readonly")
        Fun.SetControlPlace(uiName,'Entry_75',20,54,89,40)#lock
        Entry_76= EXUIControl.CustomEntry(Frame_17)
        Fun.Register(uiName,'Entry_76',Entry_76,'Entry_10')
        Entry_76.SetBGColor("#FFFFFF")
        Entry_76.SetFGColor("#000000")
        Entry_76_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_76.SetFont(Entry_76_Font)
        Entry_76.SetTipText("保存时接口的名称")
        Entry_76.SetTipFGColor("#888888")
        Entry_76.SetRelief("groove")
        Fun.SetControlPlace(uiName,'Entry_76',109,54,468,40)#lock
        ComboBox_58_Variable = Fun.AddTKVariable(uiName,'ComboBox_58')
        ComboBox_58 = tkinter.ttk.Combobox(Frame_17,textvariable=ComboBox_58_Variable, state="readonly")
        ComboBox_58_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        ComboBox_58.configure(font = ComboBox_58_Ft)
        Fun.Register(uiName,'ComboBox_58',ComboBox_58,'ComboBox_1')
        Fun.SetControlPlace(uiName,'ComboBox_58',20,159,89,40)#lock
        ComboBox_58["values"]=['GET','POST','PUT','DELETE']
        ComboBox_58.current(0)
        ComboBox_58.bind("<<ComboboxSelected>>",Fun.EventFunction_Adaptor(API_cmd.ComboBox_1_onSelect,uiName=uiName,widgetName="ComboBox_1"))
        ComboBox_74_Variable = Fun.AddTKVariable(uiName,'ComboBox_74')
        ComboBox_74 = tkinter.ttk.Combobox(Frame_17,textvariable=ComboBox_74_Variable, state="readonly")
        ComboBox_74_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=15,weight='normal',slant='roman',underline=0,overstrike=0)
        ComboBox_74.configure(font = ComboBox_74_Ft)
        Fun.Register(uiName,'ComboBox_74',ComboBox_74,'ComboBox_2')
        Fun.SetControlPlace(uiName,'ComboBox_74',104,551,320,48)#lock
        ComboBox_74["values"]=['   ']
        ComboBox_74.current(0)
        ComboBox_74.bind("<<ComboboxSelected>>",Fun.EventFunction_Adaptor(API_cmd.ComboBox_2_onSelect,uiName=uiName,widgetName="ComboBox_2"))
        RadioButton_64 = tkinter.Radiobutton(Frame_17,variable=Group_1_Variable,value=1,text="Params",anchor=tkinter.W)
        Fun.Register(uiName,'RadioButton_64',RadioButton_64,'RadioButton_1','Group_1')
        Fun.SetControlPlace(uiName,'RadioButton_64',82,256,104,40)#lock
        RadioButton_64.configure(bg = "#FFFFFF")
        RadioButton_64.configure(activebackground = "#FFFFFF")
        RadioButton_64.configure(selectcolor = "#FFFFFF")
        RadioButton_64.configure(command=lambda:API_cmd.RadioButton_1_onCommand(uiName,"RadioButton_1"))
        RadioButton_64_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        RadioButton_64.configure(font = RadioButton_64_Ft)
        RadioButton_65 = tkinter.Radiobutton(Frame_17,variable=Group_1_Variable,value=2,text="Json",anchor=tkinter.W)
        Fun.Register(uiName,'RadioButton_65',RadioButton_65,'RadioButton_2','Group_1')
        Fun.SetControlPlace(uiName,'RadioButton_65',218,256,82,40)#lock
        RadioButton_65.configure(bg = "#FFFFFF")
        RadioButton_65.configure(activebackground = "#FFFFFF")
        RadioButton_65.configure(selectcolor = "#FFFFFF")
        RadioButton_65_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        RadioButton_65.configure(font = RadioButton_65_Ft)
        RadioButton_66 = tkinter.Radiobutton(Frame_17,variable=Group_1_Variable,value=3,text="Data",anchor=tkinter.W)
        Fun.Register(uiName,'RadioButton_66',RadioButton_66,'RadioButton_3','Group_1')
        Fun.SetControlPlace(uiName,'RadioButton_66',343,256,81,40)#lock
        RadioButton_66.configure(bg = "#FFFFFF")
        RadioButton_66.configure(activebackground = "#FFFFFF")
        RadioButton_66.configure(selectcolor = "#FFFFFF")
        RadioButton_66.configure(command=lambda:API_cmd.RadioButton_3_onCommand(uiName,"RadioButton_3"))
        RadioButton_66_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        RadioButton_66.configure(font = RadioButton_66_Ft)
        Text_68 = tkinter.Text(Frame_17,undo=True,wrap=WORD)
        Fun.Register(uiName,'Text_68',Text_68,'Text_1')
        Fun.SetControlPlace(uiName,'Text_68',20,298,835,225)#lock
        Text_68.configure(bg = "#FFFFFF")
        Text_68.configure(fg = "SystemWindowText")
        Text_68.configure(relief = "sunken")
        Text_68.bind("<Key>",Fun.EventFunction_Adaptor(API_cmd.Text_1_onKey,uiName=uiName,widgetName="Text_1"))
        Text_68_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        Text_68.configure(font = Text_68_Ft)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        API_cmd.Form_1_onLoad(uiName)
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
    MyDlg = API(root)
    root.mainloop()
