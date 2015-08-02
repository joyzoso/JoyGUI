import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, \
          title=title, size=(300,250))
        panel = wx.Panel(self)

        wx.CheckBox(panel, label='Awake!', pos=(100,80))
        wx.CheckBox(panel, label='Not Awake!', pos=(100,100))


        wx.RadioButton(panel, label='Coffee!', pos=(100,10))
        wx.RadioButton(panel, label='No Coffee!', pos=(100,30))

app = wx.App()
frame = Frame("Check Box & Radio Button!")
frame.Show()
app.MainLoop()


