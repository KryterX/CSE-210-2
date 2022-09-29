def Guess(num,d):
    if d["count"]==0:
        d["lab1"].config(text="nice first guess.\n Guess again to\n truly begin.")
        d["list"][0]=int(d["ent0"].get("1.0","1.9"))
        d["count"]+=1
    else:
        d["list"][1]=int(d["ent0"].get("1.0","1.9"))
    
        if d["list"][1]== num:
            d["lab1"].config(text="You found the\n number")
        elif abs(num-d["list"][1])< abs(num-d["list"][0]):
            d["lab1"].config(text="warmer")
        
        elif abs(num-d["list"][1])== abs(num-d["list"][0]):
            d["lab1"].config(text="That's the same number")
        
        else:
            d["lab1"].config(text="colder")
        d["list"][0]=d["list"][1]
        d["list"][1]=0