# -*- coding: utf-8 -*-
'''
Created on 2013-1-15

@author: Administrator
'''

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Hello World", size=(300, 300))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        txt = wx.StaticText(panel, -1, "Hello world!")
        sizer.Add(txt, 0, wx.TOP | wx.LEFT, 100)
        self.Center()
        
class MyApp(wx.App):    # 自定义应用程序对象
    def OnInit(self):
        self.frame = MyFrame(None)
        self.frame.Show()
        idTemp = self.frame.GetId()
        print "Frame ID: ", idTemp
        return True
    
app = MyApp()
app.MainLoop()    