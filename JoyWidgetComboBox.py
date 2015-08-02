import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, \
          title=title, size=(300,250))
        panel = wx.Panel(self)

        wines = ['Pinot Noir', 'Rielsing', 'Chardonnay', 'Barbera', 'Pinot Gris']
        cb = wx.ComboBox(panel, pos=(100, 50), choices=wines, style=wx.CB_READONLY)

app = wx.App()
frame = Frame("wxPython Joy Combo Box!")
frame.Show()
app.MainLoop()


