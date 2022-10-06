import math
import _RFK as R
import level
import Game
def config_grid(width,height,d,root):
    row=math.floor(height/80)
    column=math.floor(width/80)
    d["rows"]=row
    d["col"]=column
    for l in range(row+1):
        R.Grid.rowconfigure(root,l,weight=1)
    for k in range(column):
        R.Grid.columnconfigure(root,k,weight=1)
    for i in range(row):
        for j in range(column):
            
            
            d["lab{0}".format(j+(i*column))] = R.Label(root,bd=20,highlightthickness=2,text="",bg="black",fg="blue")
            d["lab{0}".format(j+(i*column))].config(highlightbackground="black")
            d["lab{0}".format(j+(i*column))].grid(row=i+1, column=j,sticky="NSEW") 
            d["statement{0}".format(j+(i*column))]=""
    d["lab{0}".format(-1)] = R.Label(root,bd=20,highlightthickness=2,text="",bg="black",fg="white")
    d["lab{0}".format(-1)].config(highlightbackground="black")
    level.populate(d,row,column)  
    Game.start(d,row,column)   
    Game.cat(d,row,column)     
    d["lab{0}".format(-1)].grid(row=0, column=0,sticky="NSEW",columnspan=d["rows"]*5)         
