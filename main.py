from tkinter import *
import queue
import threading

class gui():
    def __init__(self,q=None):
        self.qo=queue.Queue(maxsize=1)
        self.qi=q
        self.root=Tk()

        self.root.title("ICS chat")

        self.mainframe=Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        '''
        self.name=Label(self.mainframe, text=self.peer)
        self.name.grid(column=0,row=0,padx=5,pady=5,sticky=W)
        '''
        self.display_scrollbar=Scrollbar(self.mainframe)
        self.display=Text(self.mainframe,height=35,yscrollcommand = self.display_scrollbar.set)
        self.display_scrollbar.config(command=self.display.yview)
        self.display.grid(column=0,row=1,padx=5,pady=5,sticky=(N, W, E, S))
        self.display_scrollbar.grid(column=1,row=1,sticky=(N, W, E, S))

        self.typein_scrollbar=Scrollbar(self.mainframe)
        self.typein=Text(self.mainframe,height=15,yscrollcommand = self.typein_scrollbar.set)
        self.typein_scrollbar.config(command=self.typein.yview)
        self.typein.grid(column=0,row=2,padx=5,pady=20,sticky=(N, W, E, S))
        self.typein.insert("1.0","Please type here.")
        self.typein_scrollbar.grid(column=1,row=2,sticky=(N, W, E, S))

        self.mainframe.columnconfigure(0,weight=1)
        self.mainframe.rowconfigure(1,weight=2)
        self.mainframe.rowconfigure(2,weight=1)

        self.send=Button(self.mainframe, text="Send",command=self.get_info,padx=10)
        self.send.grid(column=2,row=2,padx=10,sticky=W)

    def mainloop(self):
        self.display_thread=threading.Thread(target=self.display_info)
        self.display_thread.start()
        self.root.mainloop()

    def get_info(self):
        input=self.typein.get("1.0","end")
        self.typein.delete("1.0","end")
        self.qo.put(input.strip())
        self.qi.put(">>> "+input.strip())

    def display_info(self):
        while True:
            self.display.insert("end",self.qi.get())
            self.display.insert("end","\n\n")
            self.display.yview("end")

    def set_peer(self,peer):
        self.peer=peer

    def set_qi(self,q):
        self.qi=q


def main():
    root=gui()
    root.mainloop()

if __name__=="__main__":
    main()