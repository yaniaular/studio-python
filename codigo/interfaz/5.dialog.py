#!/usr/bin/python
# simpledialog.py

import wx

class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title)

class MyApp(wx.App):
    def OnInit(self):
        dia = MyDialog(None, -1, "simpledialog.py")
        dia.ShowModal()
        dia.Destroy()
        return True

app = MyApp(0)
app.MainLoop()
