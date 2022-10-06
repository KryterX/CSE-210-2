import random
import _RFK as R
import rands
def start(d,row,column):
    rand=random.randint(1,(row*column)-1)
    while d["lab{0}".format(rand)].cget("text") != "":
        rand=random.randint(1,(row*column))
    d["lab{0}".format(rand)].config(text="#")
    R.position[0]=rand
    
def cat(d,row,column):
    rand=random.randint(1,(row*column))
    while d["lab{0}".format(rand)].cget("text") != "":
        rand=random.randint(1,(row*column)-1)
    rand2=random.choice(rands.char)
    d["lab{0}".format(rand)].config(text=rand2)
    d["statement{0}".format(rand)]="You found the cat!!"