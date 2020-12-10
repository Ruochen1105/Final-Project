import threading
from gui import gui
from chat_client_class import *

def main():
    import argparse
    parser = argparse.ArgumentParser(description='chat client argument')
    parser.add_argument('-d', type=str, default=None, help='server IP addr')
    args = parser.parse_args()

    client_gui=gui()

    client = Client(args,client_gui.qo)
    client_gui.set_qi(client.qo)
    client_thread=threading.Thread(target=client.run_chat)
    client_thread.start()
   
    client_gui.mainloop()

main()
