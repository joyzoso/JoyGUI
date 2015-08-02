import wx

class Frame(wx.Frame):
    # Added title in parameter
    def __init__(self, title):
        #title = title variable
        wx.Frame.__init__(self, None,\
        title=title, size=(300,200))
        self.Center()
        self.Move((600,400))
        self.CreateStatusBar()


        panel = wx.Panel(self)
        button = wx.Button(panel, label="Exit", \
            size=(100,40), pos=(100,30))
        #Bind button event to the function self.exit
        button.Bind(wx.EVT_BUTTON, self.exit)

        #create menu bar
        menuBar = wx.MenuBar()
        #create the menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        self.SetMenuBar(menuBar)

        #add filemenu and editmenu to menuBar
        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")

        #add items to fileMenu
        fileMenu.Append(wx.NewId(), "Something New!", \
                        "Start yourself a new file")
        fileMenu.Append(wx.NewId(), "Open Me!", \
                        "Open a file or project")
        exitItem = fileMenu.Append(wx.NewId(), "Get Me Outta Here!", \
                        "Exit out of all this mess!")
        editMenu.Append(wx.NewId(), "Duplicate!", \
                        "Copy copy copy!")
        editMenu.Append(wx.NewId(), "Ctrl+V it",\
                        "Paste that puppy!")
        editMenu.Append(wx.NewId(), "Cut It Out!", \
                        "Ctrl+X that!")

        #bind exit menu item to exit function
        self.Bind(wx.EVT_MENU, self.exit, exitItem)

    def exit(self, event):
        self.Destroy()


app = wx.App()
#pass in the frame title
frame = Frame("Joy Python GUI")
frame.Show()
app.MainLoop()