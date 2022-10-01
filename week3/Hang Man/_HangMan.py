import random
import  tkinter as Tk
from tkinter import *
from turtle import  window_width

import Game
import Player
import Terminal
import Director
d = {}
d["count"] = 0
d["prescore"] = 0
d["list"]=[0]*2
d["strikes"]=0
window_width=500
win_width=int(window_width)
win_height=int(window_width/2)

def Setup():
    root = Tk()
    root.geometry(f"{win_width}x{win_height}")  
    root.config(background="black") 
    d["Word"] = Game.SelectWord()
    
    d["count"]=0
    d["lab{0}".format(0)] = Label(root,text="Hang Man",bd=20,highlightthickness=2)
    d["lab{0}".format(0)].config(highlightbackground="red",highlightcolor="red")
    d["lab{0}".format(0)].grid(row=0, column=2)   
    
    d["lab{0}".format(1)] = Label(root,text="",bd=20,highlightthickness=2,width=7,height=3)
    d["lab{0}".format(1)].config(highlightbackground="blue",highlightcolor="blue")
    d["lab{0}".format(1)].grid(row=1, column=1)
    
    d["lab{0}".format(1)] = Label(root,text="",bd=20,highlightthickness=2,width=7,height=3)
    d["lab{0}".format(1)].config(highlightbackground="blue",highlightcolor="blue")
    d["lab{0}".format(1)].grid(row=1, column=2)
    
    d["ent{0}".format(0)] = Text(root,highlightthickness=2,width=10,height=1)
    d["ent{0}".format(0)].config(highlightbackground="blue",highlightcolor="blue")
    d["ent{0}".format(0)].tag_configure("tag_name",justify="center")
    d["ent{0}".format(0)].tag_add("tag_name","1.0","end")
    d["ent{0}".format(0)].grid(row=1, column=3)
    
    d["but{0}".format(0)]= Button(root,text="Make Guess",padx=20,command= lambda nums=0: Player.Guess(d))
    d["but{0}".format(0)].grid(row=2,column=2,sticky="NS")
    Terminal.setup(d)
   
    
    
    
    for i in range(6): 
        Grid.rowconfigure(root,i,weight=1)
        Grid.columnconfigure(root,i,weight=1)
    
    root.mainloop()
           
     

if __name__ == "__main__":
    Setup()