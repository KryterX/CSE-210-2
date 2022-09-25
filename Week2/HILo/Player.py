import random
import Game
def draw(highlow,root,d):
    rand=random.randint(1,13)
    first_card= d["pic0"].cget("text")
    
    while rand == int(first_card):
        rand=random.randint(1,13)
        
    d["pic2"].config(text=f"{rand}")
    if highlow=="high":
        if int(d["pic2"].cget("text")) > int(d["pic0"].cget("text")):
            win_lose="win"
            Game.score(win_lose,d)
        else:
            win_lose="lose"
            Game.score(win_lose,d)
    else:
        if int(d["pic2"].cget("text")) < int(d["pic0"].cget("text")):
            win_lose="win"
            Game.score(win_lose,d)
        else:
            win_lose="lose"
            Game.score(win_lose,d)
    Game.did_win(root,d)
            
    
    
    