




def Setup(d):
    pic= " _____ \n/         \\\n\\        /\n\\    /\nO\n\\_|_/\n|\n/ \\"    
    d["lab1"].config(text=pic)
    
def Correct(d,guess):
    for x in range(len(d["Word"])):
        if guess == d["Word"][x]:
            d["Word2"][x]=f" {guess}"
    temp=""
    for x in range(len(d["Word"])):
        temp=f"{temp}{d['Word2'][x]}"
    d["lab2"].config(text=temp)
    victory=0
    for x in range(len(d["Word2"])):
        if " _" in d["Word2"][x]:
            v=1
        else:
            victory+=1
    if victory == len(d["Word2"]):
        d["lab2"].config(text=f"{d['Word']}\nYou Win")
        d["ent0"].config(state="disabled")
        d["but0"].config(state="disabled")
    
    
    
def Wrong(d,guess):
    d["strikes"]+=1
    
    temp = d["lab3"].cget("text")
    d["lab3"].config(text=f"{temp}{guess},")
    
    if d["strikes"]==1:
        d["lab1"].config(text="/         \\\n\\        /\n\\    /\nO\n\\_|_/\n|\n/ \\")
    elif d["strikes"]==2:
        d["lab1"].config(text="\\        /\n\\    /\nO\n\\_|_/\n|\n/ \\")
    elif d["strikes"]==3:
        d["lab1"].config(text="\n\\    /\nO\n\\_|_/\n|\n/ \\")
    elif d["strikes"]==4:
        d["lab1"].config(text="\nO\n\\_|_/\n|\n/ \\")
    elif d["strikes"]==5:
        d["lab1"].config(text="\nX\n\\_|_/\n|\n/ \\")
        d["lab2"].config(text="Game Over")
        d["ent0"].config(state="disabled")
        d["but0"].config(state="disabled")
        d["lab3"].config(text=f"{d['Word']}")
    