import  tkinter as tk
from tkinter import *
from tkinter import messagebox
from turtle import window_width

'''
Tic-Tac-Toe!!!
Author: Kevin Blau
'''
player=1;
count=1;
check=0;
root = Tk()
root.geometry("220x280")
screen_width=int(root.winfo_reqwidth())
screen_height = root.winfo_height()
label=tk.Label(root, text="Welcome to tic tak toe")
label.grid(row=0,column = 0,columnspan=3)
button1 = tk.Button(root,text="",bd=20,width=4,height=2,command=lambda:clicked(button1,label2))
button2 = tk.Button(root,text="",bd=20,width=4,height=2,command=lambda:clicked(button2,label2))
button3 = tk.Button(root,text="",bd=20,width=4,height=2,command=lambda:clicked(button3,label2))
button4 = tk.Button(root,text="",bd=20,width=4,height=2,command=lambda:clicked(button4,label2))
button5 = tk.Button(root,text="",bd=20,width=4,height=2,command=lambda:clicked(button5,label2))
button6 = tk.Button(root,text="",bd=20,width=4,height=2,command=lambda:clicked(button6,label2))
button7 = tk.Button(root,text="",bd=20,width=4,height=2,command=lambda:clicked(button7,label2))
button8 = tk.Button(root,text="",bd=20,width=4,height=2,command=lambda:clicked(button8,label2))
button9 = tk.Button(root,text="",bd=20,width=4,height=2,command=lambda:clicked(button9,label2))
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
label2=tk.Label(root, text=f"it is player 1's turn")
label2.grid(row=4,column = 0,columnspan=3)
def main():
    
    make_sceen();
    

def make_sceen(): 
    
    root.mainloop()
    
def clicked(button,label2):
    global player, count
    if button["text"] == "" and player == 1:
        button["text"]="X"
        winning()
        player=2
        label2["text"]=f"it is player {player}'s turn"
    elif button["text"] == "" and player == 2:
        button["text"]="O"
        winning()
        player=1
        label2["text"]=f"it is player {player}'s turn"
    else:
        messagebox.showerror("No Cheating","Try Again")
        
    
    
def winning():
    end="false"
    if button1["text"]== button2["text"] and button1["text"]==button3["text"] and (button1["text"]== "X" or button1 ["text"]=="O"):
        if button1["text"]=="X":
            win="X"
        else:
            win="O"
        end=True
        
    elif button1["text"]== button5["text"] and button1["text"]==button9["text"] and (button1["text"]== "X" or button1 ["text"]=="O"):
        if button1["text"]=="X":
            win="X"
        else:
            win="O"
        end=True
    elif button1["text"]== button4["text"] and button1["text"]==button7["text"] and (button1["text"]== "X" or button1 ["text"]=="O"):
        if button1["text"]=="X":
            win="X"
        else:
            win="O"
        end=True
    elif button2["text"]== button5["text"] and button2["text"]==button8["text"] and (button2["text"]== "X" or button2 ["text"]=="O"):
        if button2["text"]=="X":
            win="X"
        else:
            win="O"
        end=True
    elif button3["text"]== button6["text"] and button3["text"]==button9["text"] and (button3["text"]== "X" or button3 ["text"]=="O"):
        if button3["text"]=="X":
            win="X"
        else:
            win="O"
        end=True
    elif button3["text"]== button5["text"] and button3["text"]==button7["text"] and (button3["text"]== "X" or button3 ["text"]=="O"):
        if button3["text"]=="X":
            win="X"
        else:
            win="O"
        end=True
    elif button4["text"]== button5["text"] and button4["text"]==button6["text"] and (button4["text"]== "X" or button4 ["text"]=="O"):
        if button4["text"]=="X":
            win="X"
        else:
            win="O"
        end=True
    elif button7["text"]== button8["text"] and button7["text"]==button9["text"] and (button7["text"]== "X" or button7 ["text"]=="O"):
        if button7["text"]=="X":
            win="X"
        else:
            win="O"
        end=True
    if end==True:
        for i in root.winfo_children():
            i.configure(state="disabled")
        messagebox.showinfo("Winner!!!",f"{win}'s WIN!!")
        


if __name__ == "__main__":
    main()