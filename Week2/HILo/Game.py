import time
import Game
def pause(amount):
    time.sleep(amount)  
    
def score(win_lose,d):
    if win_lose=="win":
            d["pic4"].config(text="correct")
            d["score"] +=100
            score=int(d["score"])
            d["pic3"].config(text=f"score = {score}")
    else:
            d["pic4"].config(text="incorrect")
            d["score"]-=75
            score=int(d["score"])
            d["pic3"].config(text=f"score = {score}")

def did_win(root,d):  

    if d["score"] >=1000:
            d["pic4"].config(text="You win")
            d["but{0}".format(0)].config(state="disabled")
            d["but{0}".format(1)].config(state="disabled")
    elif d["score"] <=0:
            d["pic4"].config(text="You lose")
            d["but{0}".format(0)].config(state="disabled")
            d["but{0}".format(1)].config(state="disabled")
    else:    
        second_card=d["pic2"].cget("text")
        
        d["but{0}".format(0)].config(state="disabled")
        d["but{0}".format(1)].config(state="disabled")
        
        root.update()
        Game.pause(1)
        d["but{0}".format(0)].config(state="active")
        d["but{0}".format(1)].config(state="active")
        d["pic4"].config(text="Will the next card be\n higher or lower?")
        d["pic0"].config(text=f"{second_card}")
        d["pic2"].config(text="")
                  
    