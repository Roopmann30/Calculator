import wx

class CalculatorFrame(wx.Frame):
    def _init_(self):
        wx.Frame._init_(self, None, title="Simple Calculator", size=(300, 400))
        
        panel = wx.Panel(self)
        
      
        vbox = wx.BoxSizer(wx.VERTICAL)
        
      
        self.display = wx.TextCtrl(panel, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        
        
        grid = wx.GridSizer(4, 4, 10, 10)
        
     
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]
        
        for label in buttons:
            button = wx.Button(panel, label=label)
            grid.Add(button, 1, wx.EXPAND)
            button.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        
        vbox.Add(grid, proportion=1, flag=wx.EXPAND)
        panel.SetSizer(vbox)
        
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.equation = ""  
    def OnButtonClicked(self, event):
        label = event.GetEventObject().GetLabel()

        if label == 'C':
            
            self.display.Clear()
            self.equation = ""
        elif label == '=':
            try:
               
                result = eval(self.equation)
                self.display.SetValue(str(result))
                self.equation = str(result) 
            except Exception as e:
                self.display.SetValue("Error")
                self.equation = ""
        else:
            
            self.equation += label
            self.display.SetValue(self.equation)
    
    def OnClose(self, event):
       
        self.Destroy()

class CalculatorApp(wx.App):
    def OnInit(self):
        frame = CalculatorFrame()
        frame.Show()
        return True

if _name_ == "_main_":
    app = CalculatorApp()
    app.MainLoop()
