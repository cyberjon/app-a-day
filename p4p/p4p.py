#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0 on Sun Sep 29 11:59:17 2019
#

import wx
import pandas as pd
import os


# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.df=pd.DataFrame()
        self.cols=[]
        self.agg={}

        self.SetSize((472, 287))
        self.openFileDialog = wx.FileDialog(self, "Open", "", "", "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
       
        self.combo_box_1 = wx.ComboBox(self, wx.ID_ANY, choices=["Coloums"], style=wx.CB_DROPDOWN)

        self.button_2 = wx.Button(self, wx.ID_ANY, "Import")
        self.button_2.Bind(wx.EVT_BUTTON, self.ButtonImport)

        self.combo_box_2 = wx.ComboBox(self, wx.ID_ANY, choices=["", "first", "sum", "min", "max",],size=(112, 29), style=wx.CB_DROPDOWN)

        self.button_4 = wx.Button(self, wx.ID_ANY, "Add Coloum")
        self.button_4.Bind(wx.EVT_BUTTON, self.ButtonGetCols)

        self.button_1 = wx.Button(self, wx.ID_ANY, "Export")
        self.button_1.Bind(wx.EVT_BUTTON, self.ButtonExport)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("GroupBy")
        
        #self.text_ctrl_1.SetMinSize((500, 29))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(0, 3, 0, 0)
        #sizer_1.Add(self.text_ctrl_1  , 0, 0, 0)
        grid_sizer_1.Add(self.combo_box_1, 0, 0, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.combo_box_2, 0, wx.ALIGN_RIGHT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_4, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def ButtonImport(self,event):
        self.openFileDialog.ShowModal()
        self.df = pd.read_excel(self.openFileDialog.GetPath())
        self.openFileDialog.GetPath()
        self.combo_box_1.Append(self.df.columns)

    def ButtonGetCols(self,event):
       if  self.combo_box_2.GetValue() == "":
           self.cols.append(self.combo_box_1.GetValue())
           print(self.cols)
           
       if  self.combo_box_2.GetValue() != "":
           self.agg[self.combo_box_1.GetValue()]=self.combo_box_2.GetValue()
           print(self.agg)

    def ButtonExport(self,event):
<<<<<<< HEAD:p4p.py
       file_name =self.text_ctrl_1.GetValue()
       file_out=self.df.groupby(self.cols).agg(self.agg)
       file_out.reset_index(inplace=True)
       file_out.to_excel("p4p.xlsx", index=False)
=======
        file_name = os.path.expanduser("~/Desktop/p4p.xlsx")
        #file_name ='p4p.xlsx'
        file_out=self.df.groupby(self.cols).agg(self.agg)
        file_out.reset_index(inplace=True)
        file_out.to_excel(file_name, index=False)
>>>>>>> 2cccda27a3d38ab05108676b71c56f391bce136a:p4p/p4p.py
       
            
        
    
       

# end of class MyFrame

class P4P(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class P4P

if __name__ == "__main__":
    Pandas4Peopel = P4P(0)
    Pandas4Peopel.MainLoop()
