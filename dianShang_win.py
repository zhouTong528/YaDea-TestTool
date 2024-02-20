#coding=utf-8
#import libs 
import sys
import dianShang_win_cmd
import dianShang_win_sty
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
class  dianShang_win:
    def __init__(self,root,isTKroot = True):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UICommandDictionary[uiName]=dianShang_win_cmd
        Fun.Register(uiName,'root',root)
        style = dianShang_win_sty.SetupStyle()
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
        #Create the elements of root 
        Frame_3 = tkinter.Frame(Form_1)
        Fun.Register(uiName,'Frame_3',Frame_3,'Frame_1')
        Fun.SetControlPlace(uiName,'Frame_3',0,0,877,650)#lock
        Frame_3.configure(bg = "#FFFFFF")
        Frame_3.configure(relief = "flat")
        Frame_3.lower()
        LabelButton_8= EXUIControl.LabelButton(Frame_3)
        Fun.Register(uiName,'LabelButton_8',LabelButton_8,'LabelButton_2')
        LabelButton_8.SetText("物流发货")
        LabelButton_8.SetBGColor("#FFFFFF")
        LabelButton_8.SetFGColor("#FFFFFF")
        LabelButton_8_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_8.SetFont(LabelButton_8_TitleFont)
        LabelButton_8.SetBGImage("橙色按钮.png")
        LabelButton_8.SetBGColor_Hover("#FFFFFF")
        LabelButton_8.SetFGColor_Hover("#FFFFFF")
        LabelButton_8.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_8.SetBGColor_Click("#FFFFFF")
        LabelButton_8.SetFGColor_Click("#FFFFFF")
        LabelButton_8.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_8',455,549,135,48)#lock
        LabelButton_8.SetCommandFunction(dianShang_win_cmd.LabelButton_2_onCommand,self.uiName,"LabelButton_2")
        LabelButton_12= EXUIControl.LabelButton(Frame_3)
        Fun.Register(uiName,'LabelButton_12',LabelButton_12,'LabelButton_6')
        LabelButton_12.SetText("客户自提")
        LabelButton_12.SetBGColor("#FFFFFF")
        LabelButton_12.SetFGColor("#FFFFFF")
        LabelButton_12_TitleFont=tkinter.font.Font(family='Microsoft YaHei UI', size=12,weight='normal',slant='roman',underline=0,overstrike=0)
        LabelButton_12.SetFont(LabelButton_12_TitleFont)
        LabelButton_12.SetBGImage("橙色按钮.png")
        LabelButton_12.SetBGColor_Hover("#FFFFFF")
        LabelButton_12.SetFGColor_Hover("#FFFFFF")
        LabelButton_12.SetBGImage_Hover("BTN_orange_hover.png")
        LabelButton_12.SetBGColor_Click("#FFFFFF")
        LabelButton_12.SetFGColor_Click("#FFFFFF")
        LabelButton_12.SetBGImage_Click("BTN_orange_click.png")
        Fun.SetControlPlace(uiName,'LabelButton_12',668,549,135,48)#lock
        LabelButton_12.SetCommandFunction(dianShang_win_cmd.LabelButton_6_onCommand,self.uiName,"LabelButton_6")
        ListView_14 = tkinter.ttk.Treeview(Frame_3,show="headings")
        Fun.Register(uiName,'ListView_14',ListView_14,'ListView_1')
        Fun.SetControlPlace(uiName,'ListView_14',0,63,874,284)#lock
        ListView_14.configure(selectmode = "extended")
        style.configure("ListView_14.Treeview.Heading",font=('宋体', 13))
        ListView_14.config(style="ListView_14.Treeview")
        ListView_14.configure(columns = ["序号","商品名称","商品编码","库存","可用库存"])
        ListView_14.column("序号",anchor="center",width=60,stretch=True)
        ListView_14.heading("序号",anchor="center",text="序号")
        ListView_14.column("商品名称",anchor="w",width=380,stretch=True)
        ListView_14.heading("商品名称",anchor="w",text="商品名称")
        ListView_14.column("商品编码",anchor="center",width=210,stretch=True)
        ListView_14.heading("商品编码",anchor="center",text="商品编码")
        ListView_14.column("库存",anchor="center",width=90,stretch=True)
        ListView_14.heading("库存",anchor="center",text="库存")
        ListView_14.column("可用库存",anchor="center",width=120,stretch=True)
        ListView_14.heading("可用库存",anchor="center",text="可用库存")
        ListView_14.bind("<Button-1>",Fun.EventFunction_Adaptor(dianShang_win_cmd.ListView_1_onButton1,uiName=uiName,widgetName="ListView_1"))
        ListView_14_VScrollbar = tkinter.ttk.Scrollbar(ListView_14,orient=tkinter.VERTICAL)
        ListView_14_VScrollbar.place(x = 854,y = 0,width = 20,height = 284)
        ListView_14_VScrollbar.config(command = ListView_14.yview)
        ListView_14.config(yscrollcommand = ListView_14_VScrollbar.set)
        Fun.Register(uiName,'ListView_14_VScrollbar',ListView_14_VScrollbar)
        Label_15 = tkinter.Label(Frame_3,text="库存查询")
        Fun.Register(uiName,'Label_15',Label_15,'Label_1')
        Fun.SetControlPlace(uiName,'Label_15',0,7,280,48)#lock
        Label_15.configure(bg = "#FFFFFF")
        Label_15.configure(fg = "#000000")
        Label_15.configure(anchor = "w")
        Label_15.configure(relief = "flat")
        Label_15_Ft=tkinter.font.Font(family='System', size=20,weight='bold',slant='roman',underline=0,overstrike=0)
        Label_15.configure(font = Label_15_Ft)
        Label_16 = tkinter.Label(Frame_3,text="数量")
        Fun.Register(uiName,'Label_16',Label_16,'数量')
        Fun.SetControlPlace(uiName,'Label_16',31,421,104,48)
        Label_16.configure(bg = "#FFFFFF")
        Label_16.configure(fg = "SystemButtonText")
        Label_16.configure(relief = "flat")
        Label_16_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_16.configure(font = Label_16_Ft)
        Label_17 = tkinter.Label(Frame_3,text="单价")
        Fun.Register(uiName,'Label_17',Label_17,'价格')
        Fun.SetControlPlace(uiName,'Label_17',451,421,99,48)
        Label_17.configure(bg = "#FFFFFF")
        Label_17.configure(fg = "SystemButtonText")
        Label_17.configure(relief = "flat")
        Label_17_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_17.configure(font = Label_17_Ft)
        Label_18 = tkinter.Label(Frame_3,text="已选择商品")
        Fun.Register(uiName,'Label_18',Label_18,'已选择商品')
        Fun.SetControlPlace(uiName,'Label_18',-23,366,200,48)#lock
        Label_18.configure(bg = "#FFFFFF")
        Label_18.configure(fg = "SystemButtonText")
        Label_18.configure(relief = "flat")
        Label_18_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_18.configure(font = Label_18_Ft)
        Label_19 = tkinter.Label(Frame_3,text="")
        Fun.Register(uiName,'Label_19',Label_19,'展示商品')
        Fun.SetControlPlace(uiName,'Label_19',161,366,664,48)#lock
        Label_19.configure(bg = "SystemButtonFace")
        Label_19.configure(fg = "SystemButtonText")
        Label_19.configure(anchor = "w")
        Label_19.configure(relief = "flat")
        Label_19_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Label_19.configure(font = Label_19_Ft)
        Label_22 = tkinter.Label(Frame_3,text="推送电商发货订单，至当前门店，填写上面三个参数后，点击下方按钮即可！")
        Fun.Register(uiName,'Label_22',Label_22,'Label_6')
        Fun.SetControlPlace(uiName,'Label_22',62,486,749,48)#lock
        Label_22.configure(bg = "#FFFFFF")
        Label_22.configure(fg = "#CACACA")
        Label_22.configure(relief = "flat")
        Label_22_Ft=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='bold',slant='italic',underline=0,overstrike=0)
        Label_22.configure(font = Label_22_Ft)
        Label_23 = tkinter.Label(Frame_3,text="Lab")
        Fun.Register(uiName,'Label_23',Label_23,'Label_7')
        Fun.SetControlPlace(uiName,'Label_23',738,11,127,102)
        Label_23.configure(bg = "SystemButtonFace")
        Label_23.configure(fg = "SystemButtonText")
        dianShang_win_cmd.ElementBGArray[23]=Fun.LoadImageFromFile("Resources/雅迪.png",None,uiName,'Label_7')
        dianShang_win_cmd.ElementBGArray_Resize[23] = dianShang_win_cmd.ElementBGArray[23].resize((127, 102),Image.LANCZOS)
        dianShang_win_cmd.ElementBGArray_IM[23] = ImageTk.PhotoImage(dianShang_win_cmd.ElementBGArray_Resize[23])
        Label_23.configure(image = dianShang_win_cmd.ElementBGArray_IM[23])
        Label_23.configure(relief = "flat")
        Label_23.lower()
        Entry_20= EXUIControl.CustomEntry(Frame_3)
        Fun.Register(uiName,'Entry_20',Entry_20,'输入数量')
        Entry_20.SetBGColor("#FFFFFF")
        Entry_20.SetFGColor("#000000")
        Entry_20_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_20.SetFont(Entry_20_Font)
        Entry_20.SetTipFGColor("#888888")
        Entry_20.SetRelief("sunken")
        Entry_20.SetState("readonly")
        Fun.SetControlPlace(uiName,'Entry_20',161,421,200,49)#lock
        Entry_20.bind("<FocusOut>",Fun.EventFunction_Adaptor(dianShang_win_cmd.输入数量_onFocusOut,uiName=uiName,widgetName="输入数量"))
        Entry_20.bind("<Key>",Fun.EventFunction_Adaptor(dianShang_win_cmd.输入数量_onKey,uiName=uiName,widgetName="输入数量"))
        Entry_21= EXUIControl.CustomEntry(Frame_3)
        Fun.Register(uiName,'Entry_21',Entry_21,'输入价格')
        Entry_21.SetBGColor("#FFFFFF")
        Entry_21.SetFGColor("#000000")
        Entry_21_Font=tkinter.font.Font(family='Microsoft YaHei UI', size=11,weight='normal',slant='roman',underline=0,overstrike=0)
        Entry_21.SetFont(Entry_21_Font)
        Entry_21.SetTipFGColor("#888888")
        Entry_21.SetRelief("sunken")
        Fun.SetControlPlace(uiName,'Entry_21',550,421,198,49)#lock
        Entry_21.SetTextChangedFunction(dianShang_win_cmd.输入价格_onTextChanged,uiName=uiName,widgetName="输入价格")
        Entry_21.bind("<Key>",Fun.EventFunction_Adaptor(dianShang_win_cmd.输入价格_onKey,uiName=uiName,widgetName="输入价格"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        dianShang_win_cmd.Form_1_onLoad(uiName)
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
            Fun.SetControlPlace(uiName,'已选择商品',-23,366,200,48)#lock
            pass
        Fun.ActiveElement(self.uiName,event.widget)
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = dianShang_win(root)
    root.mainloop()
