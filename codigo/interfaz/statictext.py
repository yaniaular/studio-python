#!/usr/bin/python
# -*- coding: utf-8 -*-
# statictext.py

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(320, 350))

        lyrics1 = '''
    LaTex es un procesador de documentos muy 
    conveniente para la producción de 
    documentos científicos y matemáticos
    de gran calidad tipográfica.'''

        lyrics2 = "Hola curso de base de datos"

        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, lyrics1, (45, 25), style=wx.ALIGN_CENTRE)
        wx.StaticText(panel, -1, lyrics2, (45, 190), style=wx.ALIGN_CENTRE)
        self.Centre()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'statictext.py')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()
