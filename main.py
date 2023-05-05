import tkinter as tk
from interface import Interface
from timer import Timer
from message import Message

def main():
    root = tk.Tk()
    
    message_handler = Message()
    timer_handler = Timer(message_handler)
    app = Interface(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()