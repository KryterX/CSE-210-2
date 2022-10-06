import _RFK as R
import reset
def move(e,d,root):
    if e.char =="w":
        num=R.position[0]-d["col"]
        if num>-1:
            if d["lab{0}".format(num)].cget("text") == "":
                d["lab{0}".format(R.position[0])].config(text="")
                d["lab{0}".format(num)].config(text="#")
                R.position[0]=num
            else:
                statement=d["statement{0}".format(num)]
                d["lab-1"].config(text=statement)
                if statement=="You found the cat!!":
                    reset.reset(root,d)

    if e.char =="a":
        num=R.position[0]-1
        if num%d["col"]!=0:
            if d["lab{0}".format(num)].cget("text") == "":
                d["lab{0}".format(R.position[0])].config(text="")
                d["lab{0}".format(num)].config(text="#")
                R.position[0]=num
            else:
                statement=d["statement{0}".format(num)]
                d["lab-1"].config(text=statement)
        else:
            if d["statement{0}".format(num)]!="":
                statement=d["statement{0}".format(num)]
                d["lab-1"].config(text=statement)
            if statement=="You found the cat!!":
                reset.reset(root,d)
    if e.char =="s":
        num=R.position[0]+d["col"]
        if num<(d["rows"]*d["col"]):
            if d["lab{0}".format(num)].cget("text") == "":
                d["lab{0}".format(R.position[0])].config(text="")
                d["lab{0}".format(num)].config(text="#")
                R.position[0]=num
            else:
                statement=d["statement{0}".format(num)]
                d["lab-1"].config(text=statement)
                if statement=="You found the cat!!":
                    reset.reset(root,d)
    if e.char =="d":
        num=R.position[0]+1
        if num%d["col"]!=0:
            if d["lab{0}".format(num)].cget("text") == "":
                d["lab{0}".format(R.position[0])].config(text="")
                d["lab{0}".format(num)].config(text="#")
                R.position[0]=num
            else:
                statement=d["statement{0}".format(num)]
                d["lab-1"].config(text=statement)
                if statement=="You found the cat!!":
                    reset.reset(root,d)
        