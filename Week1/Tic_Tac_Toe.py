import string
import  tkinter as tk
from tkinter import *
from tkinter import messagebox
from turtle import window_width

d = {}
player=1

amount = input("how many rows and columns?: ")
arr=[0]*(1+int(amount)**2)
width=int(amount)*74
height=int(amount)*77

def prog():
    root = Tk()
    root.geometry(f"{width}x{height}")
    for x in range(1, int(amount)+1):
        for y in range(1,int(amount)+1):
            
            d["ton{0}".format((y)+(int(amount)*(x-1)))] = Button(root,text="",bd=20,width=4,height=2,command=lambda m=(y)+(int(amount)*(x-1)): clicked(d,m))
            d["ton{0}".format((y)+(int(amount)*(x-1)))].grid(row=x, column=y)
    root.mainloop()
            
        


def clicked(d,m):
    global player
    
        
    if d["ton"+str(m)].cget("text") == "" and player == 1:
        d["ton"+str(m)].config(text="X")
        arr[m]=1
        player=2
        check(arr)
    elif d["ton"+str(m)].cget("text") == "" and player == 2:
        d["ton"+str(m)].config(text="O")
        arr[m]=-1
        player=1
        check(arr)
    else:
        messagebox.showerror("No Cheating","Try Again")

def check(arr):
    global amount
    start=1
    step=1
    amount=int(amount)
    limit=amount+1
    win=""

    for x in range(1,limit):
        score=0
        for y in range(1,limit):
            score += arr[(y)+(int(amount)*(x-1))]
            
            if score == amount:
                win="X"
            elif score == amount*-1:
                win="O"
    for y in range(1,limit):
        score2=0
        for x in range(1,limit):
            score2 += arr[(y)+(int(amount)*(x-1))]
            
            if score2 == amount:
                win="X"
            elif score2 == amount*-1:
                win="O"
    score3=0
    for y in range(1,limit):
        score3 += arr[(y)+(int(amount)*((start)-1))]
        
        start+=1
        if score3 == amount:
            win="X"
        elif score3 == amount*-1:
            win="O"
    
    score4=0
    start=1
    for y in range(1,limit):
        #print((6-y)+(int(amount)*((start)-1)))
        score4 += arr[(int(amount)-y+1)+(int(amount)*((start)-1))]
        start+=1
        if score4 == amount:
            win="X"
        elif score4 == amount*-1:
            win="O"
    
        
        
    if win== "X":
        messagebox.showinfo("Winner!!!",f"{win}'s WIN!!")
        for i in range(len(d)):
           d["ton{0}".format(i+1)].configure(state="disabled")    
        
        
    elif win =="O":
        messagebox.showinfo("Winner!!!",f"{win}'s WIN!!")
        for i in range(len(d)):
               d["ton{0}".format(i+1)].configure(state="disabled") 
               
if __name__ == "__main__":
    prog()