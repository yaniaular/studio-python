#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
ZetCode wxPython tutorial
Este ejemplo muestra un Menú simple.
author: Jan Bodnar
website: www.zetcode.com
last modified: September 2011
'''
import wx

class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()
    
    def InitUI(self):
        menubar = wx.MenuBar() #objeto barra de menu
        fileMenu = wx.Menu() #objeto menu
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Salir de la \
        aplicación') #agregamos un item de menu dentro del objeto menu, fitem 
        #es el item y puede usarse para enlazarlo a un evento

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem) #vinculamos el evento del item
        #al metodo OnQuit(). cerrara las aplicaciones.

        self.SetSize((300, 200))
        self.SetTitle('Menú simple')
        self.Centre()
        self.Show(True)
    def OnQuit(self, e):
        self.Close()
def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()

