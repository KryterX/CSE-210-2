import random
import rands
import statement
def populate(d,row_num,col_num):
    total=row_num*col_num
    rand_perc=(total*(random.randint(10,15)/100))
    
    for i in range(int(rand_perc)):
        rand=random.randint(1,total-1)
        while d["lab{0}".format(rand)].cget("text") != "":
            rand=random.randint(1,total-1)
        rand2=random.choice(rands.char)
        color=random.choice(rands.colors)  
        d["lab{0}".format(rand)].config(text=f"{rand2}",fg=color)
        d["statement{0}".format(rand)]=statement.SelectSentence()    