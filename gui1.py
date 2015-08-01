import wx

class Frame(wx.Frame):
    # Added title in parameter
    def __init__(self, title):
        #title = title variable
        wx.Frame.__init__(self, None,\
        title=title, size=(300,200))
        self.Center()
        self.Move((600,400))


        panel = wx.Panel(self)
        button = wx.Button(panel, label="Exit", \
            size=(100,40), pos=(100,30))
        #Bind button event to the function self.exit
        button.Bind(wx.EVT_BUTTON, self.exit)

    def exit(self, event):
        self.Destroy()


app = wx.App()
#pass in the frame title
frame = Frame("Joy Python GUI")
frame.Show()
app.MainLoop()