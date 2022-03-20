from tkinter import *
 
from tkinter import messagebox
 
tab = Tk()
tab.title("TheMurad")
tab.geometry("600x300")
 
program = Frame(tab)
program.grid()
 
 
def dialog():
    var = messagebox.showinfo("warning" , "TheMurad")
 
button1 = Button(program, text = " Show Warning " , width=20, command=dialog)
button1.grid(padx=110, pady=80)
 

tab.mainloop()