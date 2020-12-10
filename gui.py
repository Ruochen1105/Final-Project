from tkinter import *
import queue
import threading
import time
from PIL import Image
from PIL import ImageTk
from functools import partial

class gui():
    def __init__(self,q=None):
        self.qo=queue.Queue()
        self.qi=q
        self.root=Tk()
        self.emoji_position=[]

        self.root.title("ICS chat")

        mainframe=Frame(self.root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.display_scrollbar=Scrollbar(mainframe)
        self.display=Text(mainframe,height=35,yscrollcommand = self.display_scrollbar.set)
        self.display_scrollbar.config(command=self.display.yview)
        self.display.grid(column=0,row=0,padx=5,pady=5,sticky=(N, W, E, S))
        self.display_scrollbar.grid(column=1,row=0,sticky=(N, W, E, S))

        Label(mainframe,text="Please type in below:").grid(column=0,row=1,sticky=(W,S))

        self.typein_scrollbar=Scrollbar(mainframe)
        self.typein=Text(mainframe,height=15,yscrollcommand = self.typein_scrollbar.set)
        self.typein_scrollbar.config(command=self.typein.yview)
        self.typein.grid(column=0,row=2,padx=5,pady=5,sticky=(N, W, E, S))
        self.typein_scrollbar.grid(column=1,row=2,sticky=(N, W, E, S))

        self.emoji=LabelFrame(mainframe,text="emoji",relief="sunken")
        self.emoji.grid(column=2,row=0,sticky=W)
        self.edic=dict()
        for i in range(1,8):
            image=Image.open(str(i)+".jpg")
            image=image.resize((25,25),Image.ANTIALIAS)
            emoji=ImageTk.PhotoImage(image)
            self.edic[i]=emoji
            Button(self.emoji,image=emoji,command=partial(self.type_in_emoji,i)).grid(column=(i+1)%2,row=i//2)

        mainframe.columnconfigure(0,weight=1)
        mainframe.rowconfigure(0,weight=2)
        mainframe.rowconfigure(2,weight=1)

        Button(mainframe, text="Send",command=self.get_info,padx=10).grid(column=2,row=2,padx=10,sticky=W)

        self.root.bind("<Return>",self.get_info)

    def mainloop(self):
        self.display_thread=threading.Thread(target=self.display_info)
        self.display_thread.start()
        self.root.mainloop()

    def get_info(self,event=None):
        input=self.typein.get("1.0","end").strip()
        self.typein.delete("1.0","end")
        ctime = time.strftime('%d.%m.%y,%H:%M', time.localtime())
        if len(self.emoji_position)==0:
            self.qo.put(input)            
            self.display.insert("end",ctime+" [You]>>> "+input+"\n\n")
        else:
            i=0
            input=list(input)
            for items in self.emoji_position:
                input.insert(items[0]+4*i-1,"[")
                input.insert(items[0]+4*i,"\\")
                input.insert(items[0]+4*i+1,str(items[1]))
                input.insert(items[0]+4*i+2,"]")
                i+=1
            self.emoji_position=[]
            input="".join(input)
            self.qo.put(input)
            self.display.insert("end",ctime+" [You]>>> ")
            for i in range(len(input)):
                if input[i]=="[":
                    if input[i+1]=="\\" and input[i+3]=="]":
                        self.display.image_create("end",image=self.edic[int(input[i+2])])
                elif input[i]=="\\" and input[i+1].isnumeric() and input[i+2]=="]" and input[i-1]=="[":
                    continue
                elif input[i].isnumeric() and input[i+1]=="]" and input[i-1]=="\\" and input[i-2]=="[":
                    continue
                elif input[i]=="]" and input[i-1].isnumeric() and input[i-2]=="\\" and input[i-3]=="[":
                    continue
                else:
                    self.display.insert("end",input[i])
            self.display.insert("end","\n\n")
            self.display.yview("end")

    def display_info(self):
        while True:
            input=self.qi.get()
            for i in range(len(input)):
                if input[i]=="[":
                    if input[i+1]=="\\" and input[i+3]=="]":
                        self.display.image_create("end",image=self.edic[int(input[i+2])])
                elif input[i]=="\\" and input[i+1].isnumeric() and input[i+2]=="]" and input[i-1]=="[":
                    continue
                elif input[i].isnumeric() and input[i+1]=="]" and input[i-1]=="\\" and input[i-2]=="[":
                    continue
                elif input[i]=="]" and input[i-1].isnumeric() and input[i-2]=="\\" and input[i-3]=="[":
                    continue
                else:
                    self.display.insert("end",input[i])
            self.display.insert("end","\n\n")
            self.display.yview("end")
            

    def set_qi(self,q):
        self.qi=q

    def type_in_emoji(self,i):
        self.emoji_position.append((len(self.typein.get("1.0","end")),i))
        self.typein.image_create("end",image=self.edic[i])

def main():
    root=gui()
    root.mainloop()

if __name__=="__main__":
    main()