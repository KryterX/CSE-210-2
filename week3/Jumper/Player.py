import Game

def Guess(d):
    guess = d["ent0"].get("1.0")
    Game.letter_check(guess,d)
     