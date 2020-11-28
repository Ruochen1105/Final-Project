from tkinter import *
from tkinter import ttk



root = Tk()
root.title("WeTalk")

mainframe = ttk.Frame(root,padding="5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="name").grid(column=1, row=1, sticky=W)

display=Text(mainframe,height=50,width=100)
display.grid(column=1,row=2)

typein=Text(mainframe,height=10,width=100)
typein.grid(column=1,row=3)
typein.insert("1.0","Please type here.")
input=typein.get("1.0")

ttk.Button(mainframe, text="Send").grid(column=2, row=3)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=10, pady=5)

root.mainloop()