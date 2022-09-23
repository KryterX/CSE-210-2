import  tkinter as Tk
from tkinter import *
from turtle import  window_width
import Player
d = {}
d["score"] = 0
d["count"] = 0
d["prescore"] = 0
window_width=500
win_width=int(window_width)
win_height=int(window_width/2)

def prog():
    root = Tk()
    root.geometry(f"{win_width}x{win_height}")  
    root.config(background="black") 
    score=int(d["score"])
    d["lab{0}".format(0)] = Label(root,text="Farkle",bd=20,highlightthickness=2)
    d["lab{0}".format(0)].config(highlightbackground="red",highlightcolor="red")
    d["lab{0}".format(0)].grid(row=0, column=2)   
    
    d["lab{0}".format(1)] = Label(root,text=f"Score = {score}",bd=20,highlightthickness=2,width=10)
    d["lab{0}".format(1)].config(highlightbackground="blue",highlightcolor="blue")
    d["lab{0}".format(1)].grid(row=1, column=2)
    
    d["but{0}".format(0)]= Button(root,text="",padx=20,command=lambda num=1: Player.swapdown(num,d))
    d["but{0}".format(0)].grid(row=2,column=0,sticky="NS")
    d["but{0}".format(1)]= Button(root,text="",padx=20,command=lambda num=2: Player.swapdown(num,d))
    d["but{0}".format(1)].grid(row=2,column=1,sticky="NS")
    d["but{0}".format(2)]= Button(root,text="",padx=20,command=lambda num=3: Player.swapdown(num,d))
    d["but{0}".format(2)].grid(row=2,column=2,sticky="NS")
    d["but{0}".format(3)]= Button(root,text="",padx=20,command=lambda num=4: Player.swapdown(num,d))
    d["but{0}".format(3)].grid(row=2,column=3,sticky="NS")
    d["but{0}".format(4)]= Button(root,text="",padx=20,command=lambda num=5: Player.swapdown(num,d))
    d["but{0}".format(4)].grid(row=2,column=4,sticky="NS")
    d["but{0}".format(5)]= Button(root,text="",padx=20,command=lambda num=1: Player.swapup(num,d))
    d["but{0}".format(5)].grid(row=3,column=0,sticky="NS")
    d["but{0}".format(6)]= Button(root,text="",padx=20,command=lambda num=2: Player.swapup(num,d))
    d["but{0}".format(6)].grid(row=3,column=1,sticky="NS")
    d["but{0}".format(7)]= Button(root,text="",padx=20,command=lambda num=3: Player.swapup(num,d))
    d["but{0}".format(7)].grid(row=3,column=2,sticky="NS")
    d["but{0}".format(8)]= Button(root,text="",padx=20,command=lambda num=4: Player.swapup(num,d))
    d["but{0}".format(8)].grid(row=3,column=3,sticky="NS")
    d["but{0}".format(9)]= Button(root,text="",padx=20,command=lambda num=5: Player.swapup(num,d))
    d["but{0}".format(9)].grid(row=3,column=4,sticky="NS")
    d["but{0}".format(10)] = Button(root,text="Roll",padx=20,command=lambda num=1: Player.Roll(d))
    d["but{0}".format(10)].grid(row=4,column=1,sticky="NS")
    d["but{0}".format(11)]= Button(root,text="Score",padx=20,command=lambda num=1:Player.Score(d))
    d["but{0}".format(11)].grid(row=4,column=3,sticky="NS")
    
    
    
    for i in range(6): 
        Grid.rowconfigure(root,i,weight=1)
        Grid.columnconfigure(root,i,weight=1)
    
    root.mainloop()
                 
if __name__ == "__main__":
    prog()