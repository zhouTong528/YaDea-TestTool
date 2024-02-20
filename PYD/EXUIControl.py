# 版权声明：日历控件参考CSDN博主「我的眼_001」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原作者出处链接及声明
# 原文链接：https://blog.csdn.net/wodeyan001/article/details/86703034
# -*- coding: utf-8 -*- 
import os
import tkinter
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk,ImageFont,ImageDraw
import win32gui
G_ExeDir = None
G_ResDir = None
SCALE_FACTOR = 1.5
def EventFunction_Adaptor(fun,  **params):
    """重新定义消息映射函数,自定义参数。"""
    return lambda event, fun=fun, params=params: fun(event, **params)
#图片按钮
class LabelButton:
    def __init__(self, widget):
        self.ParentWidget = widget
        self.MenuArray = []
        self.Text = 'LabelButton'
        self.BGColor = '#333333'
        self.FGColor = '#FFFFFF'
        self.Font = None 
        self.Image = None
        self.ImageFile = None
        self.BGColor_Hover = None
        self.FGColor_Hover = None
        self.Font_Hover = None 
        self.Image_Hover = None
        self.ImageFile_Hover = None
        self.BGColor_Click = None
        self.FGColor_Click = None
        self.Font_Click = None 
        self.Image_Click = None
        self.ImageFile_Click = None
        self.LabelWidth = 100
        self.LabelHeight = 24
        self.commandFunction = None
        self.uiName = None
        self.widgetName = None
        self.Anchor = "center"
        self.State = "normal"
        self.Relief = "flat"
        self.Label = tkinter.Label(self.ParentWidget,text=self.Text,width=self.LabelWidth,height=self.LabelHeight,bg = self.BGColor,highlightthickness=0,bd=0)
        self.Label.place(x=0, y=0,width=self.LabelWidth,height=self.LabelHeight)
        self.Label.bind('<Configure>',self.Configure)
        self.Label.bind('<Enter>',self.onEnter)
        self.Label.bind('<Leave>',self.onLeave)
        self.Label.bind('<Button-1>',self.onClick)
        self.Label.bind('<ButtonRelease-1>',self.onEnter)
    #取得边框样式
    def Hide(self,layout="place"):
        if layout == "pack":
            self.Label.pack_forget()
        elif layout == "grid":
            self.Label.grid_forget()
        else:
            self.Label.place_forget()
    #鼠标进入时的处理
    def onEnter(self,event):
        event.widget.configure(cursor='hand2')
        if self.Image_Hover:
            event.widget.configure(image = self.Image_Hover,compound='center')
        elif self.BGColor_Hover:
            event.widget.configure(bg = self.BGColor_Hover)
        if self.FGColor_Hover:
            event.widget.configure(fg = self.FGColor_Hover)
        if self.Font_Hover:
            event.widget.configure(font = self.Font_Hover)
        event.widget.update()
    #鼠标离开时的处理
    def onLeave(self,event):
        event.widget.configure(cursor='arrow')
        if self.Image:
            event.widget.configure(image = self.Image,compound='center')
        elif self.BGColor:
            event.widget.configure(bg = self.BGColor)
        if self.FGColor:
            event.widget.configure(fg = self.FGColor)
        if self.Font:
            event.widget.configure(font = self.Font)
        event.widget.update()
    #鼠标按下时的处理
    def onClick(self,event):
        event.widget.configure(cursor='hand2')
        if self.Image_Click:
            event.widget.configure(image = self.Image_Click,compound='center')
        elif self.BGColor_Click:
            event.widget.configure(bg = self.BGColor_Click)
        if self.FGColor_Click:
            event.widget.configure(fg = self.FGColor_Click)
        if self.Font_Click:
            event.widget.configure(font = self.Font_Click)
        event.widget.update()
        if self.commandFunction:
            self.commandFunction(self.uiName,self.widgetName)
    #设置点击事件回调处理
    def SetCommandFunction(self,Func,uiName,widgetName):
        self.commandFunction = Func
        self.uiName = uiName
        self.widgetName = widgetName
    #取得当前画布
    def GetWidget(self):
        return self.Label
    #传递绑定事件
    def bind(self,EventName,callBack):
        if self.Label:
            self.Label.bind(EventName,callBack)
    #窗口大小变化
    def Configure(self,event):
        self.Redraw()
    #设置文字内容
    def SetText(self,text):
        self.Text = text
        if self.Label:
            self.Label.configure(text = self.Text)
    #取得文字内容
    def GetText(self):
        return self.Text
    #设置文字对齐
    def SetAnchor(self,anchor):
        self.Anchor = anchor
        if self.Label:
            self.Label.configure(anchor = self.Anchor)
    #取得文字对齐
    def GetAnchor(self):
        return self.Anchor
    #设置当前是否可用
    def SetState(self,state):
        self.State = state
        if self.Label:
            self.Label.configure(state = self.State)
    #取得是否可用
    def GetState(self):
        return self.State
    #设置边框样式
    def SetRelief(self,relief):
        self.Relief = relief
        if self.Label:
            self.Label.configure(relief = self.Relief)
    #取得边框样式
    def GetRelief(self):
        return self.Relief
    #设置当前画布的背景色
    def SetBGColor(self,color):
        self.BGColor = color
        if self.Label:
            self.Label.configure(bg = self.BGColor)
    #取得当前画布的背景色
    def GetBGColor(self):
        return self.BGColor
    #设置标题栏的文字色
    def SetFGColor(self,color):
        self.FGColor = color
        if self.Label:
            self.Label.configure(fg = self.FGColor)
    #取得标题栏的文字色
    def GetFGColor(self):
        return self.FGColor
    #设置标题栏的字体
    def SetFont(self,font):
        self.Font = font
        if self.Label:
            self.Label.configure(font = self.Font)
    #取得标题栏的字体
    def GetFont(self):
        return self.Font
    #设置标题栏的字体
    def SetBGImage(self,fileName):
        global G_ExeDir
        global G_ResDir
        self.Image = None
        filePath = fileName
        if filePath and os.path.exists(filePath) == False:
            filePath = "Resources\\" + fileName
            if os.path.exists(filePath) == False:
                filePath = os.path.join(G_ExeDir,fileName)
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ResDir,fileName)
        if filePath and os.path.exists(filePath) == True:
            try:
                Image_Temp = Image.open(filePath).convert('RGBA')
                Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                self.Image = ImageTk.PhotoImage(Image_Resize)
                self.ImageFile = filePath
                if self.Label:
                    self.Label.configure(image = self.Image,compound='center')
            except:
                self.Image = None
    #取得标题栏的图片文件
    def GetBGImageFile(self):
        return self.ImageFile
    #设置鼠标悬停在标题栏时的背景色
    def SetBGColor_Hover(self,color):
        self.BGColor_Hover = color
    #取得鼠标悬停在标题栏时背景色
    def GetBGColor_Hover(self):
        return self.BGColor_Hover
    #设置鼠标悬停在标题栏时的文字色
    def SetFGColor_Hover(self,color):
        self.FGColor_Hover = color
    #取得鼠标悬停在标题栏时文字色
    def GetFGColor_Hover(self):
        return self.FGColor_Hover
    #设置标题栏的字体
    def SetFont_Hover(self,font):
        self.Font_Hover = font
    #取得标题栏的字体
    def GetFont_Hover(self):
        return self.Font_Hover
    #设置标题栏的字体
    def SetBGImage_Hover(self,fileName):
        global G_ExeDir
        global G_ResDir
        self.ImageFile_Hover = None
        filePath = fileName
        if filePath and os.path.exists(filePath) == False:
            filePath = "Resources\\" + fileName
            if os.path.exists(filePath) == False:
                filePath = os.path.join(G_ExeDir,fileName)
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ResDir,fileName)
        if filePath and os.path.exists(filePath) == True:
            try:
                Image_Temp = Image.open(filePath).convert('RGBA')
                Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                self.Image_Hover = ImageTk.PhotoImage(Image_Resize)
                self.ImageFile_Hover = filePath
            except:
                self.Image_Hover = None
    #取得标题栏的图片文件
    def GetBGImageFile_Hover(self):
        return self.ImageFile_Hover
    #设置鼠标按下标题栏时的背景色
    def SetBGColor_Click(self,color):
        self.BGColor_Click = color
        for subMenu in self.MenuArray:
            Button = subMenu[4]
            Button.configure(activebackground = self.BGColor_Click)
    #取得鼠标按下标题栏时背景色
    def GetBGColor_Click(self):
        return self.BGColor_Click
    #设置鼠标按下标题栏时的文字色
    def SetFGColor_Click(self,color):
        self.FGColor_Click = color
        for subMenu in self.MenuArray:
            Button = subMenu[4]
            Button.configure(activeforeground = self.FGColor_Click)
    #取得鼠标按下标题栏时文字色
    def GetFGColor_Click(self):
        return self.FGColor_Click
    #设置鼠标按下标题栏时字体
    def SetFont_Click(self,font):
        self.Font_Click = font
    #取得鼠标按下标题栏时字体
    def GetFont_Click(self):
        return self.Font_Click
    #设置标题栏的字体
    def SetBGImage_Click(self,fileName):
        global G_ExeDir
        global G_ResDir
        self.ImageFile_Click = None
        filePath = fileName
        if filePath and os.path.exists(filePath) == False:
            filePath = "Resources\\" + fileName
            if os.path.exists(filePath) == False:
                filePath = os.path.join(G_ExeDir,fileName)
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ResDir,fileName)
        if filePath and os.path.exists(filePath) == True:
            try:
                Image_Temp = Image.open(filePath).convert('RGBA')
                Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                self.Image_Click = ImageTk.PhotoImage(Image_Resize)
                self.ImageFile_Click = filePath
            except:
                self.Image_Click = None
    #取得标题栏的图片文件
    def GetBGImageFile_Click(self):
        return self.ImageFile_Click
    #展开
    def Redraw(self):
        self.LabelWidth = self.Label.winfo_width()
        self.LabelHeight = self.Label.winfo_height()
        if self.LabelWidth == 1 and self.LabelHeight == 1:
            self.LabelHeight = 100
            self.LabelHeight = 24
        if self.ImageFile and os.path.exists(self.ImageFile) == True:
            if self.Image.width() != self.LabelWidth or self.Image.height() != self.LabelHeight:
                try:
                    Image_Temp = Image.open(self.ImageFile).convert('RGBA')
                    Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                    self.Image = ImageTk.PhotoImage(Image_Resize)
                    if self.Label:
                        self.Label.configure(image = self.Image)
                except:
                    self.Image = None
        if self.ImageFile_Hover and os.path.exists(self.ImageFile_Hover) == True:
            if self.Image_Hover.width() != self.LabelWidth or self.Image_Hover.height() != self.LabelHeight:
                try:
                    Image_Temp = Image.open(self.ImageFile_Hover).convert('RGBA')
                    Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                    self.Image_Hover = ImageTk.PhotoImage(Image_Resize)
                except:
                    self.Image_Hover = None
        if self.ImageFile_Click and os.path.exists(self.ImageFile_Click) == True:
            if self.Image_Click.width() != self.LabelWidth or self.Image_Click.height() != self.LabelHeight:
                try:
                    Image_Temp = Image.open(self.ImageFile_Click).convert('RGBA')
                    Image_Resize = Image_Temp.resize((self.LabelWidth, self.LabelHeight),Image.LANCZOS)
                    self.Image_Click = ImageTk.PhotoImage(Image_Resize)
                except:
                    self.Image_Click = None
#圆角编辑框 
class CustomEntry:
    def __init__(self, widget):
        self.ParentWidget = widget
        self.EntryValue = tkinter.StringVar()
        self.EntryValue.set('')
        self.Canvas_width = 100
        self.Canvas_height = 24
        self.Canvas = tkinter.Canvas(self.ParentWidget,width=self.Canvas_width,height=self.Canvas_height,bg = '#FFFFFF',highlightthickness=0,bd=0)
        self.Canvas.place(x = 0, y = 0,width = 160,height=24)
        self.Entry = tkinter.Entry(self.Canvas,textvariable=self.EntryValue,background='#FFFFFF')
        self.Entry.place(x=0, y=0,width=self.Canvas_width,height=self.Canvas_height)
        self.Entry.configure(relief=tkinter.FLAT)
        self.Font = tkinter.font.Font(font='TkDefaultFont')
        self.TipText = ''
        self.TipTextColor = '#777777'
        self.TipLabel = tkinter.Label(self.Entry, text = '', justify = 'left',anchor=tkinter.W,bg='#FFFFFF')
        self.TipLabel.configure(fg = self.TipTextColor)
        self.TipLabel.bind('<Button-1>',self.onClickTip)
        self.Entry.bind('<FocusOut>',self.onResetTip)
        self.Canvas.bind('<Configure>',self.Configure)
        self.LeftIconImage = None
        self.LeftPhotoIconImage = None
        self.LeftIconImageFile = None
        self.LeftIconClickedFunction = None
        self.RightIconImage = None
        self.RightPhotoIconImage = None
        self.RightIconImageFile = None
        self.RightIconClickedFunction = None
        self.TextChangedFunction = None
        self.uiName = None
        self.widgetName = None
        self.RoundRadius = 0
        self.InnerSpacingX = 0
        self.InnerSpacingY = 0
    #取得当前编辑框宽度
    def GetWidth(self):
        return self.Canvas.winfo_width()
    #传递绑定事件
    def bind(self,EventName,callBack):
        if self.Entry:
            self.Entry.bind(EventName,callBack)
    #取得当前编辑框高度
    def GetHeight(self):
        return self.Canvas.winfo_height()
    #取得Canvas
    def GetWidget(self):
        return self.Canvas
    #取得Entry
    def GetEntry(self):
        return self.Entry
    #窗口大小变化
    def Configure(self,event):
        self.Rebuild()
    #重载一下cget
    def cget(self,attrib):
        return self.Entry.cget(attrib)
    #设置属性
    def configure(self,**kw):
        if 'text' in kw:
            self.SetText(kw['text'])
        else:
            self.Entry.configure(kw)
    #鼠标进入和离开图标时的处理
    def onIconEnter(self,event):
        event.widget.configure(cursor='hand2')
    def onIconLeave(self,event):    
        event.widget.configure(cursor='arrow')
    def onIconClick(self,event,tagName):  
        print("Click " + tagName)
        if tagName == "left_icon":
            if self.LeftIconClickedFunction:
                self.LeftIconClickedFunction(self.uiName,self.widgetName)
        else:
            if self.RightIconClickedFunction:
                self.RightIconClickedFunction(self.uiName,self.widgetName)
    #点击Tiip
    def onClickTip(self,event):
        self.TipLabel.place_forget()
        self.Entry.focus_set()
    #点击Tiip
    def onResetTip(self,event):
        if self.GetText() == '':
            self.TipLabel.place(x=0,y=0,width=self.Entry.winfo_width(),height=self.Entry.winfo_height())
    #设置左边的图标按钮
    def SetLeftIcon(self,IconFile):
        global G_ExeDir
        global G_ResDir
        filePath = IconFile
        if IconFile:
            if filePath and os.path.exists(filePath) == False:
                 filePath = "Resources\\" + IconFile
                 if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ExeDir,IconFile)
                    if os.path.exists(filePath) == False:
                        filePath = os.path.join(G_ResDir,IconFile)
            if filePath and os.path.exists(filePath) == True:
                imagePath,imageFile = os.path.split(filePath)
                try:
                    self.LeftIconImage = Image.open(filePath).convert('RGBA')
                    IconSize = self.GetHeight() - 2 * self.InnerSpacingY
                    Image_Resize = self.LeftIconImage.resize((IconSize, IconSize),Image.LANCZOS)
                    self.LeftPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
                    self.LeftIconImageFile = imageFile
                except:
                    self.LeftIconImage = None
                    self.LeftPhotoIconImage = None
                    self.LeftIconImageFile = None
        self.Redraw()
    #设置左边的图标按钮回调函数
    def SetLeftIconClickFunction(self,callBackFunc,uiName,widgetName):
        self.LeftIconClickedFunction = callBackFunc
        self.uiName = uiName
        self.widgetName = widgetName
        self.Canvas.tag_bind('left_icon','<Enter>',self.onIconEnter)
        self.Canvas.tag_bind('left_icon','<Leave>',self.onIconLeave)
        self.Canvas.tag_bind('left_icon','<Button-1>',EventFunction_Adaptor(self.onIconClick,tagName='left_icon'))
    #设置右边的图标按钮
    def SetRightIcon(self,IconFile):
        global G_ExeDir
        global G_ResDir
        filePath = IconFile
        if IconFile:
            if filePath and os.path.exists(filePath) == False:
                filePath = "Resources\\" + IconFile
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ExeDir,IconFile)
                    if os.path.exists(filePath) == False:
                        filePath = os.path.join(G_ResDir,IconFile)
            if filePath and os.path.exists(filePath) == True:
                imagePath,imageFile = os.path.split(filePath)
                try:
                    self.RightIconImage = Image.open(filePath).convert('RGBA')
                    IconSize = self.GetHeight() - 2 * self.InnerSpacingY
                    Image_Resize = self.RightIconImage.resize((IconSize, IconSize),Image.LANCZOS)
                    self.RightPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
                    self.RightIconImageFile = imageFile
                except:
                    self.RightIconImage = None
                    self.RightPhotoIconImage = None
                    self.RightIconImageFile = None
        self.Redraw()
    #设置左边的图标按钮回调函数
    def SetRightIconClickFunction(self,callBackFunc,uiName,widgetName):
        self.RightIconClickedFunction = callBackFunc
        self.uiName = uiName
        self.widgetName = widgetName
        self.Canvas.tag_bind('right_icon','<Enter>',self.onIconEnter)
        self.Canvas.tag_bind('right_icon','<Leave>',self.onIconLeave)
        self.Canvas.tag_bind('right_icon','<Button-1>',EventFunction_Adaptor(self.onIconClick,tagName='right_icon'))
    #内置的输入文本被修改时的回调函数
    def onTextChangedCallBack(self,*args):
        if self.TextChangedFunction:
            self.TextChangedFunction(self.uiName,self.widgetName,self.EntryValue.get())
    #设置输入文本被修改时的回调函数
    def SetTextChangedFunction(self,callBackFunc,uiName,widgetName):
        self.TextChangedFunction = callBackFunc
        self.uiName = uiName
        self.widgetName = widgetName
        self.EntryValue.trace('w',self.onTextChangedCallBack)
    #设置边角半径
    def SetRoundRadius(self,radius):
        self.RoundRadius = radius
        w = self.GetWidth()
        h = self.GetHeight()
        if w >= radius and h >= radius :
            HRGN = win32gui.CreateRoundRectRgn(0,0,w,h,radius,radius)
            win32gui.SetWindowRgn(self.Canvas.winfo_id(), HRGN,1)
    #取得边角半径
    def GetRoundRadius(self):
        return self.RoundRadius
    #设置横向间距
    def SetInnerSpacingX(self,InnerSpacingX):
        self.InnerSpacingX = InnerSpacingX
    #取得横向间距
    def GetInnerSpacingX(self):
        return self.InnerSpacingX
    #设置纵向间距
    def SetInnerSpacingY(self,InnerSpacingY):
        self.InnerSpacingY = InnerSpacingY
    #取得纵向间距
    def GetInnerSpacingY(self):
        return self.InnerSpacingY
    #设置文字
    def SetText(self,text):
        if text != "":
            self.TipLabel.place_forget()
        else:
            self.TipLabel.place(x=0,y=0,width=self.Entry.winfo_width(),height=self.Entry.winfo_height())
        self.EntryValue.set(text)
    #取得文字
    def GetText(self):
        return self.EntryValue.get()
    #设置字体
    def SetFont(self,font):
        self.Font = font
        self.Entry.configure(font = self.Font)
        self.TipLabel.configure(font = self.Font)
    #取得字体
    def GetFont(self):
        return self.Font
    #设置提示文字
    def SetTipText(self,text):
        self.TipText = text
        if text != '':
            self.TipLabel.place(x=0,y=0,width=self.Entry.winfo_width(),height=self.Entry.winfo_height())
            self.TipLabel.configure(bg = self.GetBGColor())
            self.TipLabel.configure(fg = self.TipTextColor)
            self.TipLabel.configure(text = self.TipText)
        else:
            self.TipLabel.place_forget()
    #取得提示文字
    def GetTipText(self):
        return self.TipText
    #设置提示文字颜色
    def SetTipFGColor(self,color):
        self.TipTextColor = color
        self.TipLabel.configure(fg=color)
    #取得提示文字颜色
    def GetTipFGColor(self):
        return self.TipTextColor
    #设置背景色
    def SetBGColor(self,bgColor):
        self.Entry.configure(bg = bgColor)
        self.TipLabel.configure(bg = bgColor)
    #取得背景色
    def GetBGColor(self):
        return self.Entry.cget('bg')
    #设置文字色
    def SetFGColor(self,fgColor):
        self.Entry.configure(fg = fgColor)
    #取得文字色
    def GetFGColor(self):
        return self.Entry.cget('fg')
    #设置替代符
    def SetShowChar(self,showChar):
        self.Entry.configure(show = showChar)
    #取得替代符
    def GetShowChar(self):
        return self.Entry.cget('show')
    #设置对齐方式
    def SetJustify(self,justify):
        self.Entry.configure(justify = justify)
    #取得对齐方式
    def GetJustify(self):
        return self.Entry.cget('justify')
    #设置样式
    def SetRelief(self,relief):
        self.Entry.configure(relief = relief)
    #取得样式
    def GetRelief(self):
        return self.Entry.cget('relief')
    #设置状态
    def SetState(self,state):
        self.Entry.configure(state = state)
    #取得状态
    def GetState(self):
        return self.Entry.cget('state')
    #重置
    def Rebuild(self):
        if self.RoundRadius > 0:
            self.SetRoundRadius(self.RoundRadius)
        IconSize = self.GetHeight()
        if self.LeftIconImage:
            Image_Resize = self.LeftIconImage.resize((IconSize, IconSize),Image.LANCZOS)
            self.LeftPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
        if self.RightIconImage:
            Image_Resize = self.RightIconImage.resize((IconSize, IconSize),Image.LANCZOS)
            self.RightPhotoIconImage = ImageTk.PhotoImage(Image_Resize)
        self.Redraw()
    #重绘
    def Redraw(self):
        AllWidth = self.GetWidth()
        IconWidth = self.GetHeight()
        if AllWidth == 1 or IconWidth == 1:
            AllWidth = 160
            IconWidth = 24
        EntryWidth = AllWidth
        EntryLeft = 0
        #左图标
        if self.LeftPhotoIconImage:
            self.Canvas.create_image(self.InnerSpacingX,self.InnerSpacingY,anchor=tkinter.NW,image=self.LeftPhotoIconImage,tag="left_icon")
            EntryWidth = EntryWidth - 2 * self.InnerSpacingX - IconWidth
            EntryLeft = 2 * self.InnerSpacingX + IconWidth
        #左图标
        if self.RightPhotoIconImage:
            self.Canvas.create_image(AllWidth - self.InnerSpacingX,self.InnerSpacingY,anchor=tkinter.NE,image=self.RightPhotoIconImage,tag="right_icon")
            EntryWidth = EntryWidth - 2 * self.InnerSpacingX - IconWidth
        self.Entry.place(x = EntryLeft , y = 0 , width = EntryWidth ,height=IconWidth)
        if self.GetText() == '' and self.TipText != '':
            self.TipLabel.place(x=0,y=0,width=EntryWidth,height=IconWidth)
#列表菜单
class ListMenu:
    def __init__(self, canvas):
        self.ParentCanvas = canvas
        self.MenuArray = []
        self.TitleHeight = 48
        self.TitleSpacingX = 0
        self.TitleSpacingY = 0
        self.TitleInnerSpacingX = 0
        self.TitleInnerSpacingY = 0
        self.TitleBGColor = '#FFFFFF'
        self.TitleFGColor = '#000000'
        self.TitleFont = tkinter.font.Font(family="Arial",size=12,weight='bold') 
        self.TitleBGColor_Hover = '#FFFFFF'
        self.TitleFGColor_Hover = '#000000'
        self.TitleFont_Hover = tkinter.font.Font(family="Arial",size=12,weight='bold')  
        self.TitleBGColor_Click = '#FFFFFF'
        self.TitleFGColor_Click = '#000000'
        self.TitleFont_Click = tkinter.font.Font(family="Arial",size=12,weight='bold')  
        self.TitleImage = None
        self.TitlePTImage = None
        self.TitleImageFile = None
        self.TitleCompound = 'left'
        self.TitleAnchor = 'left'
        self.ItemHeight = 40
        self.ItemSpacingX = 0
        self.ItemSpacingY = 0
        self.ItemInnerSpacingX = 0
        self.ItemInnerSpacingY = 0
        self.ItemBGColor = '#FFFFFF'
        self.ItemFGColor = '#000000'
        self.ItemFont = tkinter.font.Font(family="Arial",size=12,weight='normal')  
        self.ItemBGColor_Hover = '#FFFFFF'
        self.ItemFGColor_Hover = '#000000'
        self.ItemFont_Hover = tkinter.font.Font(family="Arial",size=12,weight='normal')   
        self.ItemBGColor_Click = '#FFFFFF'
        self.ItemFGColor_Click = '#000000'
        self.ItemFont_Click = tkinter.font.Font(family="Arial",size=12,weight='normal')   
        self.ItemImage = None
        self.ItemPTImage = None
        self.ItemImageFile = None
        self.ItemCompound = 'left'
        self.ItemAnchor = 'center'
        self.ExpandCharDict = {}
        self.ExpandCharDict['▼'] = ['▼','▲']
        self.ExpandCharDict['∨'] = ['∨','∧']
        self.ExpandCharDict['﹀'] = ['﹀','︿']
        self.ExpandCharDict['>'] = ['>','∨']
        self.ExpandChar = '﹀'
        self.SelectedItem = None
        self.Canvas_width = 140
        self.Canvas_height = 200
        self.Canvas_BGColor = '#FFFFFF'
        self.Canvas = tkinter.Canvas(self.ParentCanvas,width=self.Canvas_width,height=self.Canvas_height,bg = self.Canvas_BGColor ,highlightthickness=0,bd=0)
        self.Canvas.place(x=0, y=0,width=self.Canvas_width,height=self.Canvas_height)
        self.Canvas.bind('<Configure>',self.Configure)
        self.ListMenuCallBackFunction = None
        self.ListMenuUIName = None
        self.ListMenuName =  None
        self.SelectedItem = None
    #取得当前画布
    def GetWidget(self):
        return self.Canvas
    #传递绑定事件
    def bind(self,EventName,callBack):
        if self.Canvas:
            self.Canvas.bind(EventName,callBack)
    #窗口大小变化
    def Configure(self,event):
        self.Redraw()
    #取得菜单数据数组
    def GetMenuArray(self):
        return self.MenuArray
    #取得菜单数据数组的复制
    def GetMenuArray_Copy(self):
        MenuArray = []
        for subMenu in self.MenuArray:
            ChildArray = []
            for child in subMenu[2]:
                ChildArray.append([child[0],child[1],child[2],child[3],child[4],child[5],child[6],child[7]])
            MenuArray.append([subMenu[0],subMenu[1],ChildArray,subMenu[3],subMenu[4],subMenu[5],subMenu[6],subMenu[7]])
        return MenuArray
    #清空所有
    def Clear(self):
        for subMenu in self.MenuArray:
            itemList = subMenu[2]
            subMenuButton = subMenu[4]
            subMenuHandle = subMenu[5]
            subMenuClickedImage = subMenu[6]
            subMenuClickedPhotoImage = subMenu[7]
            for item in itemList:
                itemButton = item[4]
                itemHandle = item[5]
                itemClickedImage = item[6]
                itemClickedPhotoImage = item[7]
                if itemButton:
                    itemButton.destroy()
                item[4] = None
                item[5] = None
                item[6] = None
                item[7] = None
            if subMenuButton:
                subMenuButton.destroy()
            subMenu[4] = None
            subMenu[5] = None
            subMenu[6] = None
            subMenu[7] = None
            #self.Canvas.delete(subMenuHandle)
        self.MenuArray.clear()
    #设置当前画布的背景色
    def SetBGColor(self,color):
        self.Canvas_BGColor = color
        self.Canvas.configure(bg = self.Canvas_BGColor)
    #取得当前画布的背景色
    def GetBGColor(self):
        return self.Canvas_BGColor
    #设置标题横向间距
    def SetTitleSpacingX(self,spacingX):
        self.TitleSpacingX = spacingX
        self.Redraw()
    #取得标题横向间距
    def GetTitleSpacingX(self):
        return self.TitleSpacingX
    #设置标题纵向间距
    def SetTitleSpacingY(self,spacingY):
        self.TitleSpacingY = spacingY
        self.Redraw()
    #取得标题纵向间距
    def GetTitleSpacingY(self):
        return self.TitleSpacingY
    #设置标题的内部间距
    def SetTitleInnerSpacing(self,spacing):
        self.TitleInnerSpacingX = spacing
        self.TitleInnerSpacingY = spacing
        self.Redraw()
    #取得标题的内部间距
    def GetTitleInnerSpacing(self):
        return self.TitleInnerSpacingY
    #设置标题栏的背景色
    def SetTitleBGColor(self,color):
        self.TitleBGColor = color
        for subMenu in self.MenuArray:
            titleButton = subMenu[4]
            titleButton.configure(bg = color)
    #取得标题栏的背景色
    def GetTitleBGColor(self):
        return self.TitleBGColor
    #设置标题栏的文字色
    def SetTitleFGColor(self,color):
        self.TitleFGColor = color
        self.Redraw()
    def GetTitleFGColor(self):
        return self.TitleFGColor
    #设置标题栏的字体
    def SetTitleFont(self,font):
        self.TitleFont = font
        fontHeight = int(self.TitleFont.actual('size'))
        fontHeight = int((fontHeight + 8)*SCALE_FACTOR)
        if fontHeight > self.TitleHeight:
            self.TitleHeight = fontHeight
        self.Redraw()
    #取得对应标题的文本宽度
    def GetTitleTextWidth(self,itemText):
        return self.TitleFont.measure(itemText) + 2 * self.TitleInnerSpacingY
    #取得对应标题的文本高度
    def GetTitleTextHeight(self):
        fontHeight = int(self.TitleFont.actual('size'))
        fontHeight = int(fontHeight*SCALE_FACTOR)  + int(5 * SCALE_FACTOR)  + 2 * self.TitleInnerSpacingY
        return fontHeight
    #取得当前标题的宽度
    def GetTitleWidth(self,TitleIndex):
        canvasW = self.Canvas.winfo_width()
        if canvasW == 1:
            canvasW = 140
        TitleWidth = canvasW-2*self.TitleSpacingX - 2 * self.TitleInnerSpacingX
        if TitleIndex < len(self.MenuArray):
            TitleInfo = self.MenuArray[TitleIndex]
            TitleIconImage = TitleInfo[-1]
            TitleText = TitleInfo[0]
            TitleTextW = self.GetItemTextWidth(TitleText)
            RealButtonWidth = TitleTextW
            if TitleIconImage:
                TitleIconWidth = TitleIconImage.width()
                if self.TitleCompound == 'left' or self.TitleCompound == 'right':
                    RealButtonWidth = TitleTextW + TitleIconWidth + self.ItemInnerSpacingX
                else:
                    if  RealButtonWidth < TitleIconWidth:
                        RealButtonWidth = TitleIconWidth
            if TitleWidth < RealButtonWidth:
                TitleWidth = RealButtonWidth
            return TitleWidth
        return TitleWidth
    #取得当前标题的高度
    def GetTitleHeight(self,TitleIndex):
        canvasH = self.Canvas.winfo_height()
        if canvasH == 1:
            canvasH = 200
        TitleHeight = self.TitleHeight
        if TitleIndex < len(self.MenuArray):
            TitleInfo = self.MenuArray[TitleIndex]
            TitleIconImage = TitleInfo[-1]
            TitleText = TitleInfo[0]
            TitleTextH = self.GetTitleTextHeight()
            RealButtonHeight = TitleTextH
            if TitleIconImage:
                TitleIconHeight = TitleIconImage.height()
                if self.TitleCompound == 'top' or self.TitleCompound == 'bottom':
                    RealButtonHeight = TitleTextH + TitleIconHeight + self.TitleInnerSpacingY
                else:
                    if  RealButtonHeight < TitleIconHeight:
                        RealButtonHeight = TitleIconHeight
            if TitleHeight < RealButtonHeight:
                TitleHeight = RealButtonHeight
            return TitleHeight
        return TitleHeight
    #设置图标的位置
    def SetTitleCompound(self,compound):
        self.TitleCompound = compound
        self.Redraw()
    #取得设置图标的位置
    def GetTitleCompound(self):
        return self.TitleCompound
    #设置标题的锚点位置
    def SetTitleAnchor(self,anchor):
        self.TitleAnchor = anchor
        self.Redraw()
    #取得标题的锚点位置
    def GetTitleAnchor(self):
        return self.TitleAnchor
    #取得标题栏的字体
    def GetTitleFont(self):
        return self.TitleFont
    #设置鼠标悬停在标题栏时的背景色
    def SetTitleBGColor_Hover(self,color):
        self.TitleBGColor_Hover = color
    #取得鼠标悬停在标题栏时背景色
    def GetTitleBGColor_Hover(self):
        return self.TitleBGColor_Hover
    #设置鼠标悬停在标题栏时的文字色
    def SetTitleFGColor_Hover(self,color):
        self.TitleFGColor_Hover = color
    #取得鼠标悬停在标题栏时文字色
    def GetTitleFGColor_Hover(self):
        return self.TitleFGColor_Hover
    #设置标题栏的字体
    def SetTitleFont_Hover(self,font):
        self.TitleFont_Hover = font
    #取得标题栏的字体
    def GetTitleFont_Hover(self):
        return self.TitleFont_Hover
    #设置鼠标按下标题栏时的背景色
    def SetTitleBGColor_Click(self,color):
        self.TitleBGColor_Click = color
    #取得鼠标按下标题栏时背景色
    def GetTitleBGColor_Click(self):
        return self.TitleBGColor_Click
    #设置鼠标按下标题栏时的文字色
    def SetTitleFGColor_Click(self,color):
        self.TitleFGColor_Click = color
    #取得鼠标按下标题栏时文字色
    def GetTitleFGColor_Click(self):
        return self.TitleFGColor_Click
    #设置鼠标按下标题栏时字体
    def SetTitleFont_Click(self,font):
        self.TitleFont_Click = font
    #取得鼠标按下标题栏时字体
    def GetTitleFont_Click(self):
        return self.TitleFont_Click
    #设置标题栏的背景图
    def SetTitleImage(self,fileName):
        global G_ExeDir
        global G_ResDir
        self.TitleImage = None
        self.TitlePTImage = None
        canvasW = self.Canvas.winfo_width()
        canvasH = self.Canvas.winfo_height()
        if canvasW == 1 and canvasH == 1:
            canvasW = 140
            canvasH = 200
        buttonW = canvasW-2*self.TitleSpacingX
        buttonH = self.TitleHeight 
        if fileName:
            if filePath and os.path.exists(filePath) == False:
                filePath = "Resources\\" + fileName
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ExeDir,fileName)
                    if os.path.exists(filePath) == False:
                        filePath = os.path.join(G_ResDir,fileName)
            if filePath and os.path.exists(filePath) == True:
                try:
                    self.TitleImage = Image.open(filePath).convert('RGBA')
                    #Image_Resize = self.TitleImage.resize((buttonW, buttonH),Image.LANCZOS)
                    self.TitlePTImage = ImageTk.PhotoImage(self.TitleImage)
                    imagePath,imageFile = os.path.split(filePath)
                    self.TitleImageFile = imageFile
                except:
                    self.TitleImage = None
                    self.TitlePTImage = None
        self.Redraw()
    #取得标题栏的字体
    def GetTitleImageFile(self):
        return self.TitleImageFile
    #设置选项横向间距
    def SetItemSpacingX(self,spacingX):
        self.ItemSpacingX = spacingX
        self.Redraw()
    #取得选项横向间距
    def GetItemSpacingX(self):
        return self.ItemSpacingX
    #设置选项纵向间距
    def SetItemSpacingY(self,spacingY):
        self.ItemSpacingY = spacingY
        self.Redraw()
    #取得选项纵向间距
    def GetItemSpacingY(self):
        return self.ItemSpacingY
    #设置选项的间跑
    def SetItemInnerSpacing(self,spacing):
        self.ItemInnerSpacingX = spacing
        self.ItemInnerSpacingY = spacing
        self.Redraw()
    #取得选项的间隔
    def GetItemInnerSpacing(self):
        return self.ItemInnerSpacingY
    #取得对应选项的文本宽度
    def GetItemTextWidth(self,itemText):
        return self.ItemFont.measure(itemText) + 2 * self.ItemInnerSpacingX
    #取得对应选项的文本高度
    def GetItemTextHeight(self):
        fontHeight = int(self.ItemFont.actual('size'))
        fontHeight = int(fontHeight*SCALE_FACTOR)  + int(5 * SCALE_FACTOR)  + 2 * self.ItemInnerSpacingY
        return fontHeight
    #取得当前选项宽度
    def GetItemWidth(self,ItemList,ItemIndex):
        canvasW = self.Canvas.winfo_width()
        if canvasW == 1:
            canvasW = 140
        ItemWidth = canvasW-2*self.ItemSpacingX - 2 * self.ItemInnerSpacingX
        if ItemIndex < len(ItemList):
            ItemInfo = ItemList[ItemIndex]
            ItemIconImage = ItemInfo[-1]
            ItemText = ItemInfo[0]
            ItemTextW = self.GetItemTextWidth(ItemText)
            RealButtonWidth = ItemTextW
            if ItemIconImage:
                ItemIconWidth = ItemIconImage.width()
                if self.ItemCompound == 'left' or self.ItemCompound == 'right':
                    RealButtonWidth = ItemTextW + ItemIconWidth + self.ItemInnerSpacingX
                else:
                    if  RealButtonWidth < ItemIconWidth:
                        RealButtonWidth = ItemIconWidth
            if ItemWidth < RealButtonWidth:
                ItemWidth = RealButtonWidth
            return ItemWidth
        return ItemWidth
    #取得当前选项高度
    def GetItemHeight(self,ItemList,ItemIndex):
        canvasH = self.Canvas.winfo_height()
        if canvasH == 1:
            canvasH = 200
        ItemHeight = self.ItemHeight
        if ItemIndex < len(ItemList):
            ItemInfo = ItemList[ItemIndex]
            ItemIconImage = ItemInfo[-1]
            ItemText = ItemInfo[0]
            ItemTextH = self.GetItemTextHeight()
            RealButtonHeight = ItemTextH
            if ItemIconImage:
                ItemIconHeight = ItemIconImage.height()
                if self.ItemCompound == 'top' or self.ItemCompound == 'bottom':
                    RealButtonHeight = ItemTextH + ItemIconHeight + self.ItemInnerSpacingY
                else:
                    if  RealButtonHeight < ItemIconHeight:
                        RealButtonHeight = ItemIconHeight
            if ItemHeight < RealButtonHeight:
                ItemHeight = RealButtonHeight
            return ItemHeight
        return ItemHeight
    #设置子选项的背景色
    def SetItemBGColor(self,color):
        self.ItemBGColor = color
        for subMenu in self.MenuArray:
            itemList = subMenu[2]
            for item in itemList:
                itemButton = item[4]
                itemButton.configure(bg = color)
    #取得子选项背景色
    def GetItemBGColor(self):
        return self.ItemBGColor
    #设置子选项文字色
    def SetItemFGColor(self,color):
        self.ItemFGColor = color
        self.Redraw()
    #取得子选项文字色
    def GetItemFGColor(self):
        return self.ItemFGColor
    #设置子选项字体
    def SetItemFont(self,font):
        self.ItemFont = font
        fontHeight = int(self.TitleFont.actual('size'))
        fontHeight = fontHeight + 8
        fontHeight = int((fontHeight + 8)*SCALE_FACTOR)
        if fontHeight > self.ItemHeight:
            self.ItemHeight = fontHeight
        self.Redraw()
    #取得子选项的字体
    def GetItemFont(self):
        return self.ItemFont
    #设置鼠标悬停在选项的背景色
    def SetItemBGColor_Hover(self,color):
        self.ItemBGColor_Hover = color
    #取得鼠标悬停在标选项背景色
    def GetItemBGColor_Hover(self):
        return self.ItemBGColor_Hover
    #设置鼠标悬停在选项的文字色
    def SetItemFGColor_Hover(self,color):
        self.ItemFGColor_Hover = color
    #取得鼠标悬停在选项文字色
    def GetItemFGColor_Hover(self):
        return self.ItemFGColor_Hover
    #设置选项字体
    def SetItemFont_Hover(self,font):
        self.ItemFont_Hover = font
    #取得选项字体
    def GetItemFont_Hover(self):
        return self.ItemFont_Hover
    #设置鼠标按下选项背景色
    def SetItemBGColor_Click(self,color):
        self.ItemBGColor_Click = color
    #取得鼠标按下选项背景色
    def GetItemBGColor_Click(self):
        return self.ItemBGColor_Click
    #设置鼠标按下选项文字色
    def SetItemFGColor_Click(self,color):
        self.ItemFGColor_Click = color
    #取得鼠标按下选项文字色
    def GetItemFGColor_Click(self):
        return self.ItemFGColor_Click
    #设置鼠标按下选项时字体
    def SetItemFont_Click(self,font):
        self.ItemFont_Click = font
    #取得鼠标按下选项时字体
    def GetItemFont_Click(self):
        return self.ItemFont_Click
    #设置子选项的图片
    def SetItemImage(self,fileName):
        global G_ExeDir
        global G_ResDir
        self.ItemImage = None
        self.ItemPTImage = None
        canvasW = self.Canvas.winfo_width()
        canvasH = self.Canvas.winfo_height()
        if canvasW == 1 and canvasH == 1:
            canvasW = 140
            canvasH = 200
        itemW = canvasW-2*self.ItemSpacingX
        itemH = self.ItemHeight 
        if fileName:
            if filePath and os.path.exists(filePath) == False:
                filePath = "Resources\\" + fileName
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ExeDir,fileName)
                    if os.path.exists(filePath) == False:
                        filePath = os.path.join(G_ResDir,fileName)
            if filePath and os.path.exists(filePath) == True:
                try:
                    self.ItemImage = Image.open(filePath).convert('RGBA')
                    #Image_Resize = Image_Temp.resize((110, 110),Image.LANCZOS)
                    self.ItemPTImage = ImageTk.PhotoImage(self.ItemImage)
                    imagePath,imageFile = os.path.split(filePath)
                    self.ItemImageFile = imageFile
                except:
                    self.ItemImage = None
                    self.ItemPTImage = None
        else:
            for subMenu in self.MenuArray:
                itemList = subMenu[2]
                for item in itemList:
                    itemButton = item[4]
                    itemButton.delete('bgimg')
        self.Redraw()
    #取得选项的图片文件
    def GetItemImageFile(self):
        return self.ItemImageFile
    #设置选项的图标位置
    def SetItemCompound(self,compound):
        self.ItemCompound = compound
        self.Redraw()
    #取得设置图标的位置
    def GetItemCompound(self):
        return self.ItemCompound
    #设置选项的锚点位置
    def SetItemAnchor(self,anchor):
        self.ItemAnchor = anchor
        self.Redraw()
    #取得选项的锚点位置
    def GetItemAnchor(self):
        return self.ItemAnchor
    #设置标题全部展开
    def ExpandAllTitle(self,expand = True):
        for subMenu in self.MenuArray:
            subMenu[3] = expand
        self.Redraw()
    #取得标题是否展开
    def IsAllTitleExpand(self):
        for subMenu in self.MenuArray:
            if subMenu[3] == False:
                return False
        return True
    #设置标题展开
    def ExpandTitle(self,titleName,expand = True):
        for subMenu in self.MenuArray:
            if subMenu[0] == titleName:
                subMenu[3] = expand
        self.Redraw()
    #取得标题是否展开
    def IsTitleExpand(self,titleName):
        for subMenu in self.MenuArray:
            if subMenu[0] == titleName:
                return subMenu[3]
        return False
    #计算高度
    def GetTitleTop(self,index):
        Y = self.TitleSpacingY
        TitleIndex = 0
        for subMenu in self.MenuArray:
            if TitleIndex == index:
                return Y
            else:
                isExpand = subMenu[3] 
                TitleHeight = self.GetTitleHeight(TitleIndex)
                Y = Y + (TitleHeight+self.TitleSpacingY)
                if isExpand == True:
                    itemCount = len(subMenu[2])    
                    Y = Y + itemCount * (self.ItemHeight+self.ItemSpacingY)
            TitleIndex = TitleIndex + 1
        return self.TitleSpacingY
    def Title_Button1(self,event):
        for subMenu in self.MenuArray:
            if subMenu[4] == event.widget:
                self.ResetSelectedItem()
                if self.TitleBGColor_Click:
                    event.widget.configure(bg=self.TitleBGColor_Click)
                if self.TitleFGColor_Click:
                    event.widget.itemconfig('title',fill=self.TitleFGColor_Click)
                    event.widget.itemconfig('expand',fill=self.TitleFGColor_Click)
                if self.TitleFont_Click:
                    event.widget.itemconfig('title',font = self.TitleFont_Click)
                self.SelectedItem = event.widget 
    def Title_ButtonRelease1(self,event):  
        for subMenu in self.MenuArray:
            if subMenu[4] == event.widget:
                #响应展开和收缩
                subMenuName = subMenu[0]
                if type(subMenu[2]) == type([]):
                    if subMenu[3] == False:
                        subMenu[3] = True
                        self.Redraw()
                    else:
                        subMenu[3] = False
                        self.Redraw()
                elif type(subMenu[2]) == type(""):
                    print("ClickItem:"+subMenuName)
                    self.ClickItem(subMenuName,subMenu[2])
    def Title_Enter(self,event):
        event.widget.configure(cursor='hand2')
        for subMenu in self.MenuArray:
            if subMenu[4] == event.widget and self.SelectedItem != subMenu[4]:
                if self.TitleBGColor_Hover:
                    event.widget.configure(bg = self.TitleBGColor_Hover)
                if self.TitleFGColor_Hover:
                    event.widget.itemconfig('title',fill=self.TitleFGColor_Hover)
                    event.widget.itemconfig('expand',fill=self.TitleFGColor_Hover)
                if self.TitleFont_Hover:
                    event.widget.itemconfig('title',font = self.TitleFont_Hover)
    def Title_Leave(self,event):    
        event.widget.configure(cursor='arrow')
        if self.SelectedItem != event.widget:
            if self.TitleBGColor:
                event.widget.configure(bg = self.TitleBGColor)
            if self.TitleFGColor:
                event.widget.itemconfig('title',fill=self.TitleFGColor)
                event.widget.itemconfig('expand',fill=self.TitleFGColor)
            if self.TitleFont:
                event.widget.itemconfig('title',font = self.TitleFont)
    #增加一级菜单
    def AddTitle(self,titleName='',titleIcon='',titlePage=''):
        TitleCount = len(self.MenuArray)
        canvasW = self.Canvas.winfo_width()
        canvasH = self.Canvas.winfo_height()
        if canvasW == 1 and canvasH == 1:
            canvasW = 140
            canvasH = 200
        self.MenuArray.append([titleName,titleIcon,titlePage,True,None,None,None,None])
        #subMenuTag = str("submenu_%d"%TitleIndex)
        buttonX = self.TitleSpacingX
        buttonY = self.GetTitleTop(TitleCount)
        buttonW = canvasW-2*self.TitleSpacingX
        buttonH = self.TitleHeight 
        newButton = tkinter.Canvas(self.Canvas,width = buttonW,height = 20,relief=tkinter.FLAT,bg=self.TitleBGColor,highlightthickness=0,bd=0)
        newButton.place(x = buttonX,y = buttonY,width = buttonW ,height = buttonH) 
        newButton.bind('<Button-1>',self.Title_Button1)
        newButton.bind('<ButtonRelease-1>',self.Title_ButtonRelease1)
        newButton.bind('<Enter>',self.Title_Enter)
        newButton.bind('<Leave>',self.Title_Leave)
        newButton.configure(bg = self.TitleBGColor)
        submeshIconImage = None
        submeshIconPTImage = None
        if titleIcon != "":
            filePath = titleIcon
            if filePath and os.path.exists(filePath) == False:
                filePath = os.path.join(G_ExeDir,titleIcon)
                if os.path.exists(filePath) == False:
                    filePath = os.path.join(G_ResDir,titleIcon)
            if filePath and os.path.exists(filePath) == True:
                try:
                    submeshIconImage = Image.open(filePath).convert('RGBA')
                    submeshIconPTImage = ImageTk.PhotoImage(submeshIconImage)
                except:
                    pass
        buttonHandle = self.Canvas.create_window(buttonX,buttonY, window=newButton, anchor=tkinter.NW,tag="title")
        self.Canvas.itemconfig(buttonHandle,width=buttonW,height=buttonH)
        self.MenuArray[TitleCount][4] = newButton
        self.MenuArray[TitleCount][5] = buttonHandle
        self.MenuArray[TitleCount][6] = submeshIconImage
        self.MenuArray[TitleCount][7] = submeshIconPTImage
        self.RedrawTitle(TitleCount)
    #增加一级菜单(废弃，改名为AddTitle)
    def AddSubMenu(self,submenName='',submenuIcon='',submenuPage=''):
        self.AddTitle(self,submenName,submenuIcon,submenuPage)
    #删除对应标题基
    def DelTitle(self,titleName):
        subMenuIndex = 0
        for subMenu in self.MenuArray:
            if subMenu[0] == titleName:
                self.MenuArray.pop(subMenuIndex)
                break
            subMenuIndex = subMenuIndex + 1
        self.Redraw()
    def Item_Button1(self,event):
        for subMenu in self.MenuArray:
            for items in subMenu[2]:
                if items[4] == event.widget: 
                    self.ResetSelectedItem()
                    if self.ItemBGColor_Click:
                        event.widget.configure(bg = self.ItemBGColor_Click)
                    if self.ItemFGColor_Click:
                        event.widget.itemconfig('title',fill=self.ItemFGColor_Click)
                    if self.ItemFont_Click:
                        event.widget.itemconfig('title',font = self.ItemFont_Click)
                    self.SelectedItem = event.widget 
    def Item_ButtonRelease1(self,event):  
        for subMenu in self.MenuArray:
            for itemInfo in subMenu[2]:
                if itemInfo[4] == event.widget:
                    subMenuName = subMenu[0]
                    itemName = itemInfo[0]
                    itemValue = itemInfo[2]
                    print("ClickItem:"+subMenuName+" "+itemName)
                    self.ClickItem(itemName,itemValue)
    def Item_Enter(self,event):
        event.widget.configure(cursor='hand2')
        for subMenu in self.MenuArray:
            for items in subMenu[2]:
                if items[4] == event.widget and self.SelectedItem != items[4]:
                    if self.ItemBGColor_Hover:
                        event.widget.configure(bg = self.ItemBGColor_Hover)
                    if self.ItemFGColor_Hover:
                        event.widget.itemconfig('title',fill=self.ItemFGColor_Hover)
                    if self.ItemFont_Hover:
                        event.widget.itemconfig('title',font = self.ItemFont_Hover)
                    return 
    def Item_Leave(self,event):    
        event.widget.configure(cursor='arrow')
        if self.SelectedItem != event.widget:
            if self.ItemBGColor:
                event.widget.configure(bg = self.ItemBGColor)
            if self.ItemFGColor:
                event.widget.itemconfig('title',fill=self.ItemFGColor)
            if self.ItemFont:
                event.widget.itemconfig('title',font = self.ItemFont)
    #增加二级菜单（子菜单项）
    def AddItem(self,itemName='',titleName='',itemIcon='',itemPage=''):
        canvasW = self.Canvas.winfo_width()
        canvasH = self.Canvas.winfo_height()
        if canvasW == 1 and canvasH == 1:
            canvasW = 140
            canvasH = 200
        for subMenu in self.MenuArray:
            if subMenu[0] == titleName:
                if type(subMenu[2]) == type(""):
                    subMenu[2] = []
                itemCount = len(subMenu[2])
                itemTop = itemCount * (self.ItemHeight+self.ItemSpacingY)
                isExpand = subMenu[3] 
                subMeshTop = self.GetTitleTop(titleName)
                FirstItemTop = subMeshTop + (self.TitleHeight+self.TitleSpacingY)
                itemX = self.ItemSpacingX
                itemY = FirstItemTop + itemTop
                itemW = canvasW-2*self.ItemSpacingX
                itemH = self.ItemHeight 
                newItem = tkinter.Canvas(self.Canvas,width = itemW,height = itemH,relief=tkinter.FLAT,bg=self.ItemBGColor,highlightthickness=0,bd=0)
                newItem.place(x = itemX,y = itemY,width = itemW ,height = itemH ) 
                newItem.bind('<Button-1>',self.Item_Button1)
                newItem.bind('<ButtonRelease-1>',self.Item_ButtonRelease1)
                newItem.bind('<Enter>',self.Item_Enter)
                newItem.bind('<Leave>',self.Item_Leave)
                newItem.configure(bg = self.ItemBGColor)
                ItemImage = None
                ItemPhotoImage = None
                if itemIcon != "":
                    filePath = itemIcon
                    if filePath and os.path.exists(filePath) == False:
                        filePath = os.path.join(G_ExeDir,itemIcon)
                        if os.path.exists(filePath) == False:
                            filePath = os.path.join(G_ResDir,itemIcon)
                    if filePath and os.path.exists(filePath) == True:
                        try:
                            ItemImage = Image.open(filePath).convert('RGBA')
                            ItemPhotoImage = ImageTk.PhotoImage(ItemImage)
                        except:
                            pass
                itemHandle = self.Canvas.create_window(itemX,itemY, window=newItem, anchor=tkinter.NW,tag="item")
                if isExpand == True:
                    self.Canvas.itemconfig(itemHandle,width=itemW,height=itemH)
                else:
                    self.Canvas.itemconfig(itemHandle,width=0,height=0)
                subMenu[2].append([itemName,itemIcon,itemPage,itemTop,newItem,itemHandle,ItemImage,ItemPhotoImage])
                self.RedrawItem(subMenu[2],itemCount)
                return 
    #删除对应标题基
    def DelItem(self,titleName,itemName):
        subMenuIndex = 0
        for subMenu in self.MenuArray:
            if subMenu[0] == titleName:
                itemIndex = 0
                for Item in subMenu[2]:
                    if Item[0] == itemName:
                        subMenu[2].pop(itemIndex)
                        break
                    itemIndex = itemIndex + 1
                break
        self.Redraw()
    #点击标题按钮
    def ClickTitleButton(self,subMenuName):
        canvasW = self.Canvas.winfo_width()
        canvasH = self.Canvas.winfo_height()
        if canvasW == 1 and canvasH == 1:
            canvasW = 140
            canvasH = 200
        for subMenu in self.MenuArray:
            if subMenu[0] == subMenuName:
                subMeshTop = self.GetSubMenuY(subMenuName)
                if subMenu[3] == False:
                    subMenu[3] = True
                    self.Redraw()
                else:
                    subMenu[3] = False
                    self.Redraw()
    #绘制一个按钮
    def RedrawTitle(self,TitleIndex,TitleState='Normal'):
        canvasW = self.Canvas.winfo_width()
        if canvasW == 1:
            canvasW = 140
        InitTitleWidth = canvasW-2*self.TitleSpacingX - 2 * self.TitleInnerSpacingX
        if TitleIndex >= 0 and TitleIndex < len(self.MenuArray):
            ButtonInfo = self.MenuArray[TitleIndex]
            TitleText = ButtonInfo[0]
            TitlePTIconImage = ButtonInfo[-1]
            TitleButton = ButtonInfo[4]
            TitleWidth = InitTitleWidth
            TitleHeight = self.TitleHeight + 2 * self.TitleInnerSpacingY
            TitleTextW = self.GetTitleTextWidth(TitleText)
            TitleTextH = self.GetTitleTextHeight()
            TitleIconWidth = 0
            TitleIconHeight = 0
            if TitlePTIconImage:                
                TitleIconWidth = TitlePTIconImage.width() + self.TitleInnerSpacingX
                TitleIconHeight = TitlePTIconImage.height() + self.TitleInnerSpacingY
            RealButtonWidth = TitleTextW 
            if self.TitleCompound == 'left' or self.TitleCompound == 'right':
                RealButtonWidth = TitleTextW + TitleIconWidth
            else:
                if  RealButtonWidth < TitleIconWidth:
                    RealButtonWidth = TitleIconWidth
            RealButtonHeight = TitleTextH 
            if self.TitleCompound == 'top' or self.TitleCompound == 'bottom':
                RealButtonHeight = TitleTextH + TitleIconHeight
            else:
                if  RealButtonHeight < TitleIconHeight:
                    RealButtonHeight = TitleIconHeight
            if TitleWidth < RealButtonWidth:
                TitleWidth = RealButtonWidth
            if TitleHeight < RealButtonHeight:
                TitleHeight = RealButtonHeight
            centerX = int(TitleWidth/2)
            centerY = int(TitleHeight/2)
            if TitleState == "Click":
                if self.TitleBGColor_Click:
                    TitleButton.configure(bg = self.TitleBGColor_Click)
                TitleButton.delete('all')
                if self.TitlePTImage:
                    TitleButton.create_image(0,0,anchor=tkinter.NW,image=self.TitlePTImage,tag="bgimg")
                #图标
                if TitlePTIconImage:
                    if self.TitleCompound == 'left':
                        #跟据锚点位置计算X位置
                        leftX = self.TitleInnerSpacingX 
                        if self.TitleAnchor == "center":
                            leftX = int((TitleWidth - TitleIconWidth - TitleTextW)/2)
                        elif self.TitleAnchor == "right":
                            leftX = TitleWidth - self.TitleInnerSpacingX - TitleIconWidth - TitleTextW
                        TitleButton.create_image(leftX ,centerY,anchor=tkinter.W,image=TitlePTIconImage,tag="icon")
                        TitleButton.create_text(leftX + TitleIconWidth,centerY, font=self.TitleFont_Click,anchor=tkinter.W,fill=self.TitleFGColor_Click,text=TitleText,tag='title') 
                    elif self.TitleCompound == 'right':
                        #跟据锚点位置计算X位置
                        leftX = self.TitleInnerSpacingX 
                        if self.TitleAnchor == "center":
                            leftX = int((TitleWidth - TitleIconWidth - TitleTextW)/2)
                        elif self.TitleAnchor == "right":
                            leftX = TitleWidth - self.TitleInnerSpacingX - TitleIconWidth - TitleTextW
                        TitleButton.create_text(leftX,centerY, font=self.TitleFont_Click,anchor=tkinter.W,fill=self.TitleFGColor_Click,text=TitleText,tag='title') 
                        TitleButton.create_image(leftX + TitleIconWidth,centerY,anchor=tkinter.W,image=TitlePTIconImage,tag="icon")
                    elif self.TitleCompound == 'top':
                        ContentWidth = TitleTextW
                        if TitleTextW < TitleIconWidth:
                            ContentWidth = TitleIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.TitleInnerSpacingX + int(ContentWidth/2)
                        if self.TitleAnchor == "center":
                            centerX = int(TitleWidth/2)
                        elif self.TitleAnchor == "right":
                            centerX = TitleWidth - self.TitleInnerSpacingX - int(ContentWidth/2)
                        TitleButton.create_image(centerX,self.TitleInnerSpacingY,anchor=tkinter.N,image=TitlePTIconImage,tag="icon")
                        TitleButton.create_text(centerX,self.TitleInnerSpacingY + TitleIconHeight, font=self.TitleFont_Click,anchor=tkinter.N,fill=self.TitleFGColor_Click,text=TitleText,tag='title') 
                    elif self.TitleCompound == 'bottom':
                        ContentWidth = TitleTextW
                        if TitleTextW < TitleIconWidth:
                            ContentWidth = TitleIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.TitleInnerSpacingX + int(ContentWidth/2)
                        if self.TitleAnchor == "center":
                            centerX = int(TitleWidth/2)
                        elif self.TitleAnchor == "right":
                            centerX = TitleWidth - self.TitleInnerSpacingX - int(ContentWidth/2)
                        TitleButton.create_text(centerX,TitleHeight - self.TitleInnerSpacingY-TitleIconHeight - TitleTextH, font=self.TitleFont_Click,anchor=tkinter.N,fill=self.TitleFGColor_Click,text=TitleText,tag='title') 
                        TitleButton.create_image(centerX,TitleHeight - self.TitleInnerSpacingY-TitleIconHeight ,anchor=tkinter.N,image=TitlePTIconImage,tag="icon")
                    elif self.TitleCompound == 'center':
                        TitleButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=TitlePTIconImage,tag="icon")
                        TitleButton.create_text(centerX,centerY, font=self.TitleFont_Click,anchor=tkinter.CENTER,fill=self.TitleFGColor_Click,text=TitleText,tag='title') 
                    else:
                        TitleButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=TitlePTIconImage,tag="icon")
                else:
                    #跟据锚点位置计算X位置
                    leftX = self.TitleInnerSpacingX 
                    if self.TitleAnchor == "center":
                        leftX = int(TitleWidth - TitleTextW)/2
                    elif self.TitleAnchor == "right":
                        leftX = TitleWidth - self.TitleInnerSpacingX - TitleTextW
                    TitleButton.create_text(leftX,centerY, font=self.TitleFont_Click,anchor=tkinter.W,fill=self.TitleFGColor_Click,text=TitleText,tag='title')  
            elif TitleState == "Hover":
                if self.TitleBGColor_Hover:
                    TitleButton.configure(bg = self.TitleBGColor_Hover)
                TitleButton.delete('all')
                if self.TitlePTImage:
                    TitleButton.create_image(0,0,anchor=tkinter.NW,image=self.TitlePTImage,tag="bgimg")
                #图标
                if TitlePTIconImage:
                    if self.TitleCompound == 'left':
                        #跟据锚点位置计算X位置
                        leftX = self.TitleInnerSpacingX 
                        if self.TitleAnchor == "center":
                            leftX = int((TitleWidth - TitleIconWidth - TitleTextW)/2)
                        elif self.TitleAnchor == "right":
                            leftX = TitleWidth - self.TitleInnerSpacingX - TitleIconWidth - TitleTextW
                        TitleButton.create_image(leftX ,centerY,anchor=tkinter.W,image=TitlePTIconImage,tag="icon")
                        TitleButton.create_text(leftX + TitleIconWidth,centerY, font=self.TitleFont_Hover,anchor=tkinter.W,fill=self.TitleFGColor_Hover,text=TitleText,tag='title') 
                    elif self.TitleCompound == 'right':
                        #跟据锚点位置计算X位置
                        leftX = self.TitleInnerSpacingX 
                        if self.TitleAnchor == "center":
                            leftX = int((TitleWidth - TitleIconWidth - TitleTextW)/2)
                        elif self.TitleAnchor == "right":
                            leftX = TitleWidth - self.TitleInnerSpacingX - TitleIconWidth - TitleTextW
                        TitleButton.create_text(leftX,centerY, font=self.TitleFont_Hover,anchor=tkinter.W,fill=self.TitleFGColor_Hover,text=TitleText,tag='title') 
                        TitleButton.create_image(leftX + TitleIconWidth,centerY,anchor=tkinter.W,image=TitlePTIconImage,tag="icon")
                    elif self.TitleCompound == 'top':
                        ContentWidth = TitleTextW
                        if TitleTextW < TitleIconWidth:
                            ContentWidth = TitleIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.TitleInnerSpacingX + int(ContentWidth/2)
                        if self.TitleAnchor == "center":
                            centerX = int(TitleWidth/2)
                        elif self.TitleAnchor == "right":
                            centerX = TitleWidth - self.TitleInnerSpacingX - int(ContentWidth/2)
                        TitleButton.create_image(centerX,self.TitleInnerSpacingY,anchor=tkinter.N,image=TitlePTIconImage,tag="icon")
                        TitleButton.create_text(centerX,self.TitleInnerSpacingY + TitleIconHeight, font=self.TitleFont_Hover,anchor=tkinter.N,fill=self.TitleFGColor_Hover,text=TitleText,tag='title') 
                    elif self.TitleCompound == 'bottom':
                        ContentWidth = TitleTextW
                        if TitleTextW < TitleIconWidth:
                            ContentWidth = TitleIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.TitleInnerSpacingX + int(ContentWidth/2)
                        if self.TitleAnchor == "center":
                            centerX = int(TitleWidth/2)
                        elif self.TitleAnchor == "right":
                            centerX = TitleWidth - self.TitleInnerSpacingX - int(ContentWidth/2)
                        TitleButton.create_text(centerX,TitleHeight - self.TitleInnerSpacingY-TitleIconHeight - TitleTextH, font=self.TitleFont_Hover,anchor=tkinter.N,fill=self.TitleFGColor_Hover,text=TitleText,tag='title') 
                        TitleButton.create_image(centerX,TitleHeight - self.TitleInnerSpacingY-TitleIconHeight ,anchor=tkinter.N,image=TitlePTIconImage,tag="icon")
                    elif self.TitleCompound == 'center':
                        TitleButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=TitlePTIconImage,tag="icon")
                        TitleButton.create_text(centerX,centerY, font=self.TitleFont_Hover,anchor=tkinter.CENTER,fill=self.TitleFGColor_Hover,text=TitleText,tag='title') 
                    else:
                        TitleButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=TitlePTIconImage,tag="icon")
                else:
                    #跟据锚点位置计算X位置
                    leftX = self.TitleInnerSpacingX 
                    if self.TitleAnchor == "center":
                        leftX = int(TitleWidth - TitleTextW)/2
                    elif self.TitleAnchor == "right":
                        leftX = TitleWidth - self.TitleInnerSpacingX - TitleTextW
                    TitleButton.create_text(leftX,centerY, font=self.TitleFont_Hover,anchor=tkinter.W,fill=self.TitleFGColor_Hover,text=TitleText,tag='title')  
            else:
                if self.TitleBGColor:
                    TitleButton.configure(bg = self.TitleBGColor)
                TitleButton.delete('all')
                if self.TitlePTImage:
                    TitleButton.create_image(0,0,anchor=tkinter.NW,image=self.TitlePTImage,tag="bgimg")
                #图标
                if TitlePTIconImage:
                    if self.TitleCompound == 'left':
                        #跟据锚点位置计算X位置
                        leftX = self.TitleInnerSpacingX 
                        if self.TitleAnchor == "center":
                            leftX = int((TitleWidth - TitleIconWidth - TitleTextW)/2)
                        elif self.TitleAnchor == "right":
                            leftX = TitleWidth - self.TitleInnerSpacingX - TitleIconWidth - TitleTextW
                        TitleButton.create_image(leftX ,centerY,anchor=tkinter.W,image=TitlePTIconImage,tag="icon")
                        TitleButton.create_text(leftX + TitleIconWidth,centerY, font=self.TitleFont,anchor=tkinter.W,fill=self.TitleFGColor,text=TitleText,tag='title') 
                    elif self.TitleCompound == 'right':
                        #跟据锚点位置计算X位置
                        leftX = self.TitleInnerSpacingX 
                        if self.TitleAnchor == "center":
                            leftX = int((TitleWidth - TitleIconWidth - TitleTextW)/2)
                        elif self.TitleAnchor == "right":
                            leftX = TitleWidth - self.TitleInnerSpacingX - TitleIconWidth - TitleTextW
                        TitleButton.create_text(leftX,centerY, font=self.TitleFont,anchor=tkinter.W,fill=self.TitleFGColor,text=TitleText,tag='title') 
                        TitleButton.create_image(leftX + TitleIconWidth,centerY,anchor=tkinter.W,image=TitlePTIconImage,tag="icon")
                    elif self.TitleCompound == 'top':
                        ContentWidth = TitleTextW
                        if TitleTextW < TitleIconWidth:
                            ContentWidth = TitleIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.TitleInnerSpacingX + int(ContentWidth/2)
                        if self.TitleAnchor == "center":
                            centerX = int(TitleWidth/2)
                        elif self.TitleAnchor == "right":
                            centerX = TitleWidth - self.TitleInnerSpacingX - int(ContentWidth/2)
                        TitleButton.create_image(centerX,self.TitleInnerSpacingY,anchor=tkinter.N,image=TitlePTIconImage,tag="icon")
                        TitleButton.create_text(centerX,self.TitleInnerSpacingY + TitleIconHeight, font=self.TitleFont,anchor=tkinter.N,fill=self.TitleFGColor,text=TitleText,tag='title') 
                    elif self.TitleCompound == 'bottom':
                        ContentWidth = TitleTextW
                        if TitleTextW < TitleIconWidth:
                            ContentWidth = TitleIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.TitleInnerSpacingX + int(ContentWidth/2)
                        if self.TitleAnchor == "center":
                            centerX = int(TitleWidth/2)
                        elif self.TitleAnchor == "right":
                            centerX = TitleWidth - self.TitleInnerSpacingX - int(ContentWidth/2)
                        TitleButton.create_text(centerX,TitleHeight - self.TitleInnerSpacingY-TitleIconHeight-TitleTextH, font=self.TitleFont,anchor=tkinter.N,fill=self.TitleFGColor,text=TitleText,tag='title') 
                        TitleButton.create_image(centerX,TitleHeight - self.TitleInnerSpacingY-TitleIconHeight ,anchor=tkinter.N,image=TitlePTIconImage,tag="icon")
                    elif self.TitleCompound == 'center':
                        TitleButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=TitlePTIconImage,tag="icon")
                        TitleButton.create_text(centerX,centerY, font=self.TitleFont,anchor=tkinter.CENTER,fill=self.TitleFGColor,text=TitleText,tag='title') 
                    else:
                        TitleButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=TitlePTIconImage,tag="icon")
                else:
                    #跟据锚点位置计算X位置
                    leftX = self.TitleInnerSpacingX 
                    if self.TitleAnchor == "center":
                        leftX = int(TitleWidth - TitleTextW)/2
                    elif self.TitleAnchor == "right":
                        leftX = TitleWidth - self.TitleInnerSpacingX - TitleTextW
                    TitleButton.create_text(leftX,centerY, font=self.TitleFont,anchor=tkinter.W,fill=self.TitleFGColor,text=TitleText,tag='title')  
    #绘制一个按钮
    def RedrawItem(self,ItemList,ItemIndex,ItemState='Normal'):
        canvasW = self.Canvas.winfo_width()
        if canvasW == 1:
            canvasW = 140
        InitItemWidth = canvasW-2*self.ItemSpacingX - 2 * self.ItemInnerSpacingX
        if ItemIndex >= 0 and ItemIndex < len(ItemList):
            ButtonInfo = ItemList[ItemIndex]
            ItemText = ButtonInfo[0]
            ItemPTIconImage = ButtonInfo[-1]
            ItemButton = ButtonInfo[4]
            ItemWidth = InitItemWidth
            ItemHeight = self.ItemHeight + 2 * self.ItemInnerSpacingY
            ItemTextW = self.GetItemTextWidth(ItemText)
            ItemTextH = self.GetItemTextHeight()
            ItemIconWidth = 0
            ItemIconHeight = 0
            if ItemPTIconImage:                
                ItemIconWidth = ItemPTIconImage.width() + self.ItemInnerSpacingX
                ItemIconHeight = ItemPTIconImage.height() + self.ItemInnerSpacingY
            RealButtonWidth = ItemTextW 
            if self.ItemCompound == 'left' or self.ItemCompound == 'right':
                RealButtonWidth = ItemTextW + ItemIconWidth
            else:
                if  RealButtonWidth < ItemIconWidth:
                    RealButtonWidth = ItemIconWidth
            RealButtonHeight = ItemTextH 
            if self.ItemCompound == 'top' or self.ItemCompound == 'bottom':
                RealButtonHeight = ItemTextH + ItemIconHeight
            else:
                if  RealButtonHeight < ItemIconHeight:
                    RealButtonHeight = ItemIconHeight
            if ItemWidth < RealButtonWidth:
                ItemWidth = RealButtonWidth
            if ItemHeight < RealButtonHeight:
                ItemHeight = RealButtonHeight
            centerX = int(ItemWidth/2)
            centerY = int(ItemHeight/2)
            if ItemState == "Click":
                if self.ItemBGColor_Click:
                    ItemButton.configure(bg = self.ItemBGColor_Click)
                ItemButton.delete('all')
                if self.ItemPTImage:
                    ItemButton.create_image(0,0,anchor=tkinter.NW,image=self.ItemPTImage,tag="bgimg")
                #图标
                if ItemPTIconImage:
                    if self.ItemCompound == 'left':
                        #跟据锚点位置计算X位置
                        leftX = self.ItemInnerSpacingX 
                        if self.ItemAnchor == "center":
                            leftX = int((ItemWidth - ItemIconWidth - ItemTextW)/2)
                        elif self.ItemAnchor == "right":
                            leftX = ItemWidth - self.ItemInnerSpacingX - ItemIconWidth - ItemTextW
                        ItemButton.create_image(leftX ,centerY,anchor=tkinter.W,image=ItemPTIconImage,tag="icon")
                        ItemButton.create_text(leftX + ItemIconWidth,centerY, font=self.ItemFont_Click,anchor=tkinter.W,fill=self.ItemFGColor_Click,text=ItemText,tag='title') 
                    elif self.ItemCompound == 'right':
                        #跟据锚点位置计算X位置
                        leftX = self.ItemInnerSpacingX 
                        if self.ItemAnchor == "center":
                            leftX = int((ItemWidth - ItemIconWidth - ItemTextW)/2)
                        elif self.ItemAnchor == "right":
                            leftX = ItemWidth - self.ItemInnerSpacingX - ItemIconWidth - ItemTextW
                        ItemButton.create_text(leftX,centerY, font=self.ItemFont_Click,anchor=tkinter.W,fill=self.ItemFGColor_Click,text=ItemText,tag='title') 
                        ItemButton.create_image(leftX + ItemIconWidth,centerY,anchor=tkinter.W,image=ItemPTIconImage,tag="icon")
                    elif self.ItemCompound == 'top':
                        ContentWidth = ItemTextW
                        if ItemTextW < ItemIconWidth:
                            ContentWidth = ItemIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.ItemInnerSpacingX + int(ContentWidth/2)
                        if self.ItemAnchor == "center":
                            centerX = int(ItemWidth/2)
                        elif self.ItemAnchor == "right":
                            centerX = ItemWidth - self.ItemInnerSpacingX - int(ContentWidth/2)
                        ItemButton.create_image(centerX,self.ItemInnerSpacingY,anchor=tkinter.N,image=ItemPTIconImage,tag="icon")
                        ItemButton.create_text(centerX,self.ItemInnerSpacingY + ItemIconHeight, font=self.ItemFont_Click,anchor=tkinter.N,fill=self.ItemFGColor_Click,text=ItemText,tag='title') 
                    elif self.ItemCompound == 'bottom':
                        ContentWidth = ItemTextW
                        if ItemTextW < ItemIconWidth:
                            ContentWidth = ItemIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.ItemInnerSpacingX + int(ContentWidth/2)
                        if self.ItemAnchor == "center":
                            centerX = int(ItemWidth/2)
                        elif self.ItemAnchor == "right":
                            centerX = ItemWidth - self.ItemInnerSpacingX - int(ContentWidth/2)
                        ItemButton.create_text(centerX,ItemHeight - self.ItemInnerSpacingY-ItemIconHeight - ItemTextH, font=self.ItemFont_Click,anchor=tkinter.N,fill=self.ItemFGColor_Click,text=ItemText,tag='title') 
                        ItemButton.create_image(centerX,ItemHeight - self.ItemInnerSpacingY-ItemIconHeight ,anchor=tkinter.N,image=ItemPTIconImage,tag="icon")
                    elif self.ItemCompound == 'center':
                        ItemButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=ItemPTIconImage,tag="icon")
                        ItemButton.create_text(centerX,centerY, font=self.ItemFont_Click,anchor=tkinter.CENTER,fill=self.ItemFGColor_Click,text=ItemText,tag='title') 
                    else:
                        ItemButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=ItemPTIconImage,tag="icon")
                else:
                    #跟据锚点位置计算X位置
                    leftX = self.ItemInnerSpacingX 
                    if self.ItemAnchor == "center":
                        leftX = int((ItemWidth - ItemTextW)/2)
                    elif self.ItemAnchor == "right":
                        leftX = ItemWidth - self.ItemInnerSpacingX - ItemTextW
                    ItemButton.create_text(leftX,centerY, font=self.ItemFont_Click,anchor=tkinter.W,fill=self.ItemFGColor_Click,text=ItemText,tag='title')  
            elif ItemState == "Hover":
                if self.ItemBGColor_Hover:
                    ItemButton.configure(bg = self.ItemBGColor_Hover)
                ItemButton.delete('all')
                if self.ItemPTImage:
                    ItemButton.create_image(0,0,anchor=tkinter.NW,image=self.ItemPTImage,tag="bgimg")
                #图标
                if ItemPTIconImage:
                    if self.ItemCompound == 'left':
                        #跟据锚点位置计算X位置
                        leftX = self.ItemInnerSpacingX 
                        if self.ItemAnchor == "center":
                            leftX = int((ItemWidth - ItemIconWidth - ItemTextW)/2)
                        elif self.ItemAnchor == "right":
                            leftX = ItemWidth - self.ItemInnerSpacingX - ItemIconWidth - ItemTextW
                        ItemButton.create_image(leftX ,centerY,anchor=tkinter.W,image=ItemPTIconImage,tag="icon")
                        ItemButton.create_text(leftX + ItemIconWidth,centerY, font=self.ItemFont_Hover,anchor=tkinter.W,fill=self.ItemFGColor_Hover,text=ItemText,tag='title') 
                    elif self.ItemCompound == 'right':
                        #跟据锚点位置计算X位置
                        leftX = self.ItemInnerSpacingX 
                        if self.ItemAnchor == "center":
                            leftX = int((ItemWidth - ItemIconWidth - ItemTextW)/2)
                        elif self.ItemAnchor == "right":
                            leftX = ItemWidth - self.ItemInnerSpacingX - ItemIconWidth - ItemTextW
                        ItemButton.create_text(leftX,centerY, font=self.ItemFont_Hover,anchor=tkinter.W,fill=self.ItemFGColor_Hover,text=ItemText,tag='title') 
                        ItemButton.create_image(leftX + ItemIconWidth,centerY,anchor=tkinter.W,image=ItemPTIconImage,tag="icon")
                    elif self.ItemCompound == 'top':
                        ContentWidth = ItemTextW
                        if ItemTextW < ItemIconWidth:
                            ContentWidth = ItemIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.ItemInnerSpacingX + int(ContentWidth/2)
                        if self.ItemAnchor == "center":
                            centerX = int(ItemWidth/2)
                        elif self.ItemAnchor == "right":
                            centerX = ItemWidth - self.ItemInnerSpacingX - int(ContentWidth/2)
                        ItemButton.create_image(centerX,self.ItemInnerSpacingY,anchor=tkinter.N,image=ItemPTIconImage,tag="icon")
                        ItemButton.create_text(centerX,self.ItemInnerSpacingY + ItemIconHeight, font=self.ItemFont_Hover,anchor=tkinter.N,fill=self.ItemFGColor_Hover,text=ItemText,tag='title') 
                    elif self.ItemCompound == 'bottom':
                        ContentWidth = ItemTextW
                        if ItemTextW < ItemIconWidth:
                            ContentWidth = ItemIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.ItemInnerSpacingX + int(ContentWidth/2)
                        if self.ItemAnchor == "center":
                            centerX = int(ItemWidth/2)
                        elif self.ItemAnchor == "right":
                            centerX = ItemWidth - self.ItemInnerSpacingX - int(ContentWidth/2)
                        ItemButton.create_text(centerX,ItemHeight - self.ItemInnerSpacingY-ItemIconHeight - ItemTextH, font=self.ItemFont_Hover,anchor=tkinter.N,fill=self.ItemFGColor_Hover,text=ItemText,tag='title') 
                        ItemButton.create_image(centerX,ItemHeight - self.ItemInnerSpacingY-ItemIconHeight ,anchor=tkinter.N,image=ItemPTIconImage,tag="icon")
                    elif self.ItemCompound == 'center':
                        ItemButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=ItemPTIconImage,tag="icon")
                        ItemButton.create_text(centerX,centerY, font=self.ItemFont_Hover,anchor=tkinter.CENTER,fill=self.ItemFGColor_Hover,text=ItemText,tag='title') 
                    else:
                        ItemButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=ItemPTIconImage,tag="icon")
                else:
                    #跟据锚点位置计算X位置
                    leftX = self.ItemInnerSpacingX 
                    if self.ItemAnchor == "center":
                        leftX = int(ItemWidth - ItemTextW)/2
                    elif self.ItemAnchor == "right":
                        leftX = ItemWidth - self.ItemInnerSpacingX - ItemTextW
                    ItemButton.create_text(leftX,centerY, font=self.ItemFont_Hover,anchor=tkinter.W,fill=self.ItemFGColor_Hover,text=ItemText,tag='title')  
            else:
                if self.ItemBGColor:
                    ItemButton.configure(bg = self.ItemBGColor)
                ItemButton.delete('all')
                if self.ItemPTImage:
                    ItemButton.create_image(0,0,anchor=tkinter.NW,image=self.ItemPTImage,tag="bgimg")
                #图标
                if ItemPTIconImage:
                    if self.ItemCompound == 'left':
                        #跟据锚点位置计算X位置
                        leftX = self.ItemInnerSpacingX 
                        if self.ItemAnchor == "center":
                            leftX = int((ItemWidth - ItemIconWidth - ItemTextW)/2)
                        elif self.ItemAnchor == "right":
                            leftX = ItemWidth - self.ItemInnerSpacingX - ItemIconWidth - ItemTextW
                        ItemButton.create_image(leftX ,centerY,anchor=tkinter.W,image=ItemPTIconImage,tag="icon")
                        ItemButton.create_text(leftX + ItemIconWidth,centerY, font=self.ItemFont,anchor=tkinter.W,fill=self.ItemFGColor,text=ItemText,tag='title') 
                    elif self.ItemCompound == 'right':
                        #跟据锚点位置计算X位置
                        leftX = self.ItemInnerSpacingX 
                        if self.ItemAnchor == "center":
                            leftX = int((ItemWidth - ItemIconWidth - ItemTextW)/2)
                        elif self.ItemAnchor == "right":
                            leftX = ItemWidth - self.ItemInnerSpacingX - ItemIconWidth - ItemTextW
                        ItemButton.create_text(leftX,centerY, font=self.ItemFont,anchor=tkinter.W,fill=self.ItemFGColor,text=ItemText,tag='title') 
                        ItemButton.create_image(leftX + ItemIconWidth,centerY,anchor=tkinter.W,image=ItemPTIconImage,tag="icon")
                    elif self.ItemCompound == 'top':
                        ContentWidth = ItemTextW
                        if ItemTextW < ItemIconWidth:
                            ContentWidth = ItemIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.ItemInnerSpacingX + int(ContentWidth/2)
                        if self.ItemAnchor == "center":
                            centerX = int(ItemWidth/2)
                        elif self.ItemAnchor == "right":
                            centerX = ItemWidth - self.ItemInnerSpacingX - int(ContentWidth/2)
                        ItemButton.create_image(centerX,self.ItemInnerSpacingY,anchor=tkinter.N,image=ItemPTIconImage,tag="icon")
                        ItemButton.create_text(centerX,self.ItemInnerSpacingY + ItemIconHeight, font=self.ItemFont,anchor=tkinter.N,fill=self.ItemFGColor,text=ItemText,tag='title') 
                    elif self.ItemCompound == 'bottom':
                        ContentWidth = ItemTextW
                        if ItemTextW < ItemIconWidth:
                            ContentWidth = ItemIconWidth
                        #跟据锚点位置计算X位置
                        centerX = self.ItemInnerSpacingX + int(ContentWidth/2)
                        if self.ItemAnchor == "center":
                            centerX = int(ItemWidth/2)
                        elif self.ItemAnchor == "right":
                            centerX = ItemWidth - self.ItemInnerSpacingX - int(ContentWidth/2)
                        ItemButton.create_text(centerX,ItemHeight - self.ItemInnerSpacingY-ItemIconHeight - ItemTextH, font=self.ItemFont,anchor=tkinter.N,fill=self.ItemFGColor,text=ItemText,tag='title') 
                        ItemButton.create_image(centerX,ItemHeight - self.ItemInnerSpacingY-ItemIconHeight ,anchor=tkinter.N,image=ItemPTIconImage,tag="icon")
                    elif self.ItemCompound == 'center':
                        ItemButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=ItemPTIconImage,tag="icon")
                        ItemButton.create_text(centerX,centerY, font=self.ItemFont,anchor=tkinter.CENTER,fill=self.ItemFGColor,text=ItemText,tag='title') 
                    else:
                        ItemButton.create_image(centerX,centerY,anchor=tkinter.CENTER,image=ItemPTIconImage,tag="icon")
                else:
                    #跟据锚点位置计算X位置
                    leftX = self.ItemInnerSpacingX 
                    if self.ItemAnchor == "center":
                        leftX = int((ItemWidth - ItemTextW)/2)
                    elif self.ItemAnchor == "right":
                        leftX = ItemWidth - self.ItemInnerSpacingX - ItemTextW
                    ItemButton.create_text(leftX,centerY, font=self.ItemFont,anchor=tkinter.W,fill=self.ItemFGColor,text=ItemText,tag='title')  
    #展开
    def Redraw(self):
        canvasW = self.Canvas.winfo_width()
        canvasH = self.Canvas.winfo_height()
        if canvasW == 1 and canvasH == 1:
            canvasW = 140
            canvasH = 200
        TopY = self.TitleSpacingY
        TitleIndex = 0
        for subMenu in self.MenuArray:
            itemList = subMenu[2]
            isExpand = subMenu[3] 
            subMenuButton = subMenu[4]
            subMenuHandle = subMenu[5]
            TitleX = self.TitleSpacingX
            TitleY = TopY
            TitleWidth = self.GetTitleWidth(TitleIndex)
            TitleHeight = self.GetTitleHeight(TitleIndex)
            if self.SelectedItem == subMenuButton:
                self.RedrawTitle(TitleIndex,TitleState='Click')
            else:
                self.RedrawTitle(TitleIndex,TitleState='Normal')
            self.Canvas.coords(subMenuHandle,TitleX,TitleY)
            self.Canvas.itemconfig(subMenuHandle,width=TitleWidth,height=TitleHeight)
            TopY = TopY + self.GetTitleHeight(TitleIndex) + self.TitleSpacingY
            if isExpand == True:
                # if self.ExpandChar != '' and itemList:
                #     subMenuButton.delete('expand')
                #     subMenuButton.create_text(TitleWidth - self.TitleSpacingX ,int(self.TitleHeight/2), font=self.TitleFont,anchor=tkinter.E,fill=self.TitleFGColor,text=self.ExpandCharDict[self.ExpandChar][0],tag='expand')  
                ItemIndex = 0
                for item in itemList:
                    itemButton = item[4]
                    itemHandle = item[5]
                    ItemX = self.ItemSpacingX
                    ItemY = TopY
                    ItemWidth = self.GetItemWidth(itemList,ItemIndex)
                    ItemHeight = self.GetItemHeight(itemList,ItemIndex)
                    if self.SelectedItem == itemButton:
                        self.RedrawItem(itemList,ItemIndex,ItemState='Click')
                    else:
                        self.RedrawItem(itemList,ItemIndex,ItemState='Normal')
                    itemButton.place(x=ItemX,y=ItemY,width=ItemWidth,height=ItemHeight)
                    self.Canvas.coords(itemHandle,ItemX,ItemY)
                    self.Canvas.itemconfig(itemHandle,width=ItemWidth,height=ItemHeight)
                    TopY = TopY + self.GetItemHeight(itemList,ItemIndex) + self.ItemSpacingY 
                    ItemIndex = ItemIndex + 1
                TopY = TopY + self.TitleSpacingY 
            else:
                # if self.ExpandChar != '' and itemList:
                #     subMenuButton.delete('expand')
                #     subMenuButton.create_text(buttonW - self.TitleSpacingX ,int(self.TitleHeight/2), font=self.TitleFont,anchor=tkinter.E,fill=self.TitleFGColor,text=self.ExpandCharDict[self.ExpandChar][1],tag='expand')  
                for item in itemList:
                    itemButton = item[4]
                    itemHandle = item[5]
                    itemButton.place_forget()
                    self.Canvas.coords(itemHandle,-999,-999)
                    self.Canvas.itemconfig(itemHandle,width=0,height=0)
            TitleIndex = TitleIndex + 1 
    #点击展开或收缩
    def ClickItem(self,itemName,itemPage=''):
        print("ClickItem:"+itemName+" "+itemPage)
        if self.ListMenuCallBackFunction:
            self.ListMenuCallBackFunction(self.ListMenuUIName,self.ListMenuName,itemName,itemPage)
    #设置点击确定时的回调函数
    def SetListMenuCallBackFunction(self,callBackFun,classname,widgetname):
        self.ListMenuCallBackFunction = callBackFun
        self.ListMenuUIName = classname
        self.ListMenuName = widgetname
    #重置
    def ResetSelectedItem(self):
        for subMenu in self.MenuArray:
            if subMenu[4] == self.SelectedItem:
                if self.TitleBGColor:
                    self.SelectedItem.configure(bg = self.TitleBGColor)
                if self.TitleFGColor:
                    self.SelectedItem.itemconfig('title',fill=self.TitleFGColor)
                    self.SelectedItem.itemconfig('expand',fill=self.TitleFGColor)
                if self.TitleFont:
                    self.SelectedItem.itemconfig('title',font = self.TitleFont)
                    return 
            for items in subMenu[2]:
                if items[4] == self.SelectedItem:
                    if self.ItemBGColor:
                        self.SelectedItem.configure(bg = self.ItemBGColor)
                    if self.ItemFGColor:
                        self.SelectedItem.itemconfig('title',fill=self.ItemFGColor)
                    if self.ItemFont:
                        self.SelectedItem.itemconfig('title',font = self.ItemFont)
                    return 
