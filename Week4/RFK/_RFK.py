from cProfile import label
from logging import config
import random
import  tkinter as Tk
from tkinter import *
import math
from tkinter import messagebox
import setup
import Player
position=[0]
win_width=int(random.randint(1000,2000))
win_height=int(random.randint(500,1000))
d={}

    
def main():
    root = Tk()
    root.geometry(f"{win_width}x{win_height}")
    root.bind("<KeyPress>",lambda event: Player.move(event,d,root))
    root.focus_set()
    setup.config_grid(win_width,win_height,d,root)
    root.mainloop()
           

    




    



if __name__ == "__main__":
    main()