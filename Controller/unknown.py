#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#    Feb 07, 2020 12:53:22 PM GMT  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import unknown_support
import UI_implementor as PathUi
import GUI as EchoRt

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def funcExe(self):
        print("this was not supposed to be called")

        

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font13 = "-family Fixedsys -size 43 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family Fixedsys -size 22 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family Fixedsys -size 36 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("744x567+518+176")
        top.title("Echo Controller")
        top.configure(background="#ffffff")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=-0.027, rely=0.3, height=404, width=804)
        self.Label1.configure(background="#fffcff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="#000000")
        self._img1 = tk.PhotoImage(file="../../../../../../Pictures/coderdojo/vector-hills-pixel-6.png")
        self.Label1.configure(image=self._img1)
        self.Label1.configure(text='''Echo Controller''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.363, rely=0.265, height=68, width=190)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#41ff3b")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font14)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''New Path''')

        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(relx=0.363, rely=0.441, height=68, width=190)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#41ff3b")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font=font14)
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''EchoRt''')

        self.Button1_3 = tk.Button(top)
        self.Button1_3.place(relx=0.228, rely=0.617, height=63, width=186)
        self.Button1_3.configure(activebackground="#ececec")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="#41ff3b")
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(font=font14)
        self.Button1_3.configure(foreground="#000000")
        self.Button1_3.configure(highlightbackground="#d9d9d9")
        self.Button1_3.configure(highlightcolor="black")
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''Options''')
        self.Button1_3.configure(width=186)
        self.Button1.configure(command= self.funcExe)

        self.Button1_4 = tk.Button(top)
        self.Button1_4.place(relx=0.524, rely=0.617, height=63, width=186)
        self.Button1_4.configure(activebackground="#ececec")
        self.Button1_4.configure(activeforeground="#000000")
        self.Button1_4.configure(background="#41ff3b")
        self.Button1_4.configure(disabledforeground="#a3a3a3")
        self.Button1_4.configure(font=font14)
        self.Button1_4.configure(foreground="#000000")
        self.Button1_4.configure(highlightbackground="#d9d9d9")
        self.Button1_4.configure(highlightcolor="black")
        self.Button1_4.configure(pady="0")
        self.Button1_4.configure(text='''Vcontrol''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.685, rely=0.265, height=156, width=172)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(borderwidth="0")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self._img2 = tk.PhotoImage(file="../../../../../../Pictures/coderdojo/Untitled-1.png")
        self.Label2.configure(image=self._img2)
        self.Label2.configure(text='''joystick''')
        self.Label2.configure(underline="0")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.121, rely=0.035, height=81, width=606)
        self.Label3.configure(background="#fff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font15)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Echo Controller''')

if __name__ == '__main__':
    vp_start_gui()





