from tkinter import *
import time

root=Tk()
root.title("ICS chat")

mainframe=Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

name=Label(mainframe, text="name")
name.grid(column=0,row=0,padx=5,pady=5,sticky=W)

display=Text(mainframe,height=35)
display.grid(column=0,row=1,padx=5,pady=5,sticky=(N, W, E, S))

typein=Text(mainframe,height=15)
typein.grid(column=0,row=2,padx=5,pady=20,sticky=(N, W, E, S))
typein.insert("1.0","Please type here.")
#input=typein.get("1.0","end")
#typein.delete("1.0","end")

mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(1,weight=1)

send=Button(mainframe, text="Send",padx=10)
send.grid(column=1,row=2,padx=10,sticky=W)

root.mainloop()