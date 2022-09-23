import Game
import random
def swapup(num,d):
    
    first_num=d["but{0}".format(num+4)].cget("text")
    if first_num!="":
        d["but{0}".format(num-1)].config(text=first_num)
        d["but{0}".format(num+4)].config(text="")
        Game.double_check(d)
    
def swapdown(num,d):
    first_num=d["but{0}".format(num-1)].cget("text")
    if first_num!="":
        d["but{0}".format(num+4)].config(text=first_num)
        d["but{0}".format(num-1)].config(text="")  
        Game.double_check(d)
        
def Roll(d):
    if d["count"]==0:
        for i in range(5):
            rand = random.randint(1,6)
            d["but{0}".format(i+5)].config(text=rand)
        Game.first_check(d)
    d["count"]+=1
    
def Score(d):
    d["score"]+=d["prescore"]
    for i in range(10):
        d["but{0}".format(i)].config(text="")
    d["count"]=0
    score=d["score"]
    d["lab1"].config(text=f"score = {score}")
    d["prescore"]=0