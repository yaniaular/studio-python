#!/usr/bin/python
# simple.py
import wx # importar el modulo wxPython
app = wx.App() #el objeto aplicacion
frame = wx.Frame(None, -1, 'simple.py')
frame.Show() # muestra el frame en la pantalla
app.MainLoop() #ciclo sin fin, captura y envia todos los eventos a lo largo de la aplicacion

