import tkinter as tk
import Controller

controller_class = Controller.ControllerCl()

class CntGUI():
    def closingWindow(self):
        self.mw.quit()

    def __init__(self, master):
        self.mw = master
        self.mw.option_add("*Button.Background", "white")
        self.mw.option_add("*Button.Foreground", "blue")
        self.mw.title('Controller')
        self.mw.geometry("500x500") 
        self.mw.resizable(0, 0) 
        self.back = tk.Frame(master=self.mw, bg="white")
        self.back.pack_propagate(0)
        self.back.pack(fill=tk.BOTH, expand=1) 
        self.info = tk.Label(master=self.back, text='Controller Client', bg="white", fg="black")
        self.info.pack(fill=tk.X, padx=0, pady = 0)
        self.option1 = tk.Button(master=self.back, text='froward', command=controller_class.forward)
        self.option1.pack(pady=15)
        self.option2 = tk.Button(master=self.back, text='backward', command=controller_class.backward)
        self.option2.pack(pady=15)

        

def startUp():
        mw = tk.Tk()
        b = CntGUI(mw)
        mw.mainloop()
startUp()



