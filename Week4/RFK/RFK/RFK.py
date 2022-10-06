from cProfile import label
import random
import  tkinter as Tk
from tkinter import *
import math
char = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","'","(",")"]
position=[0]
win_width=int(random.randint(1000,2000))
win_height=int(random.randint(500,1000))
d={}

    
def main():
    root = Tk()
    root.geometry(f"{win_width}x{win_height}")
    root.bind("<KeyPress>",lambda event: move(event,d))
    root.focus_set()
    config_grid(win_width,win_height,d,root)
    root.mainloop()
           
def populate(d,row_num,col_num):
    total=row_num*col_num
    rand_perc=(total*(random.randint(15,20)/100))
    
    for i in range(int(rand_perc)):
        rand=random.randint(1,total-1)
        while d["lab{0}".format(rand)].cget("text") != "":
            rand=random.randint(1,total)
        rand2=random.choice(char)
        d["lab{0}".format(rand)].config(text=f"{rand2}")
            
    
def change_window(root):
    win_width=int(random.randint(500,1000))
    win_height=int(random.randint(500,1000))
    root.geometry(f"{win_width}x{win_height}")

def config_grid(width,height,d,root):
    row=math.floor(height/80)
    column=math.floor(width/80)
    d["rows"]=row
    d["col"]=column
    for l in range(row+1):
        Grid.rowconfigure(root,l,weight=1)
    for k in range(column):
        Grid.columnconfigure(root,k,weight=1)
    for i in range(row):
        for j in range(column):
            
              
            d["lab{0}".format(j+(i*column))] = Label(root,bd=20,highlightthickness=2,text="")
            d["lab{0}".format(j+(i*column))].config(highlightbackground="black")
            d["lab{0}".format(j+(i*column))].grid(row=i+1, column=j,sticky="NSEW") 
    d["lab{0}".format(-1)] = Label(root,bd=20,highlightthickness=2,text="")
    d["lab{0}".format(-1)].config(highlightbackground="black")
    d["lab{0}".format(-1)].grid(row=0, column=5,sticky="NSEW") 
    populate(d,row,column)  
    start(d,row,column)        
            
def move(e,d):
    if e.char =="w":
        num=position[0]-d["col"]
        if num>-1:
            if d["lab{0}".format(num)].cget("text") == "":
                d["lab{0}".format(position[0])].config(text="")
                d["lab{0}".format(num)].config(text="#")
                position[0]=num
            else:
                d["lab-1"].config(text="it works")
        print("Move Up")
    if e.char =="a":
        num=position[0]-1
        if num%d["col"]!=0:
            if d["lab{0}".format(num)].cget("text") == "":
                d["lab{0}".format(position[0])].config(text="")
                d["lab{0}".format(num)].config(text="#")
                position[0]=num
            else:
                print("get comment")
        print("Move Left"),e.char
    if e.char =="s":
        num=position[0]+d["col"]
        if num<(d["rows"]*d["col"]):
            if d["lab{0}".format(num)].cget("text") == "":
                d["lab{0}".format(position[0])].config(text="")
                d["lab{0}".format(num)].config(text="#")
                position[0]=num
            else:
                print("get comment")
        print("Move Down"),e.char
    if e.char =="d":
        num=position[0]+1
        if num%d["col"]!=0:
            if d["lab{0}".format(num)].cget("text") == "":
                d["lab{0}".format(position[0])].config(text="")
                d["lab{0}".format(num)].config(text="#")
                position[0]=num
            else:
                print("get comment")
        print("Move Right"),e.char
        
def start(d,row,column):
    rand=random.randint(1,(row*column))
    while d["lab{0}".format(rand)].cget("text") != "":
        rand=random.randint(1,(row*column))
    d["lab{0}".format(rand)].config(text="#")
    position[0]=rand
    
if __name__ == "__main__":
    main()