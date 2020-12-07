import threading
from main import gui
from chat_client_class import *

def main():
    import argparse
    parser = argparse.ArgumentParser(description='chat client argument')
    parser.add_argument('-d', type=str, default=None, help='server IP addr')
    args = parser.parse_args()

    
    client = Client(args)

    client_thread=threading.Thread(target=client.run_chat)
    client_thread.start()
    client_gui=gui()
    client_gui.mainloop()

main()
