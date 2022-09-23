from tkinter import messagebox

def first_check(d):
    check=0
    for i in range(5):
        num= int(d["but{0}".format(i+5)].cget("text"))
        if num==1 or num==5:
            check=1
    if check!=1:
        messagebox.showinfo("Farkle","Farkle")
        

    
def double_check(d):
    prescore=0
    for i in range(5):
        if d["but{0}".format(i)].cget("text")==1:
            prescore+=100
        if d["but{0}".format(i)].cget("text")==5:
            prescore+=50
    score=d["score"]
    d["prescore"]=prescore
    d["lab{0}".format(1)].config(text=f"score = {score} +{prescore}")   