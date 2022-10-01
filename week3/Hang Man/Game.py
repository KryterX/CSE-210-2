import random
import _HangMan
import Terminal

def SelectWord():
    with open("E:\Programming\Python\CSE-210-1\week3\Hang Man\WordSelect.txt","r") as f:
        Lines=f.read().splitlines()
        random_line=random.choice(Lines)
        print(random_line)
        return random_line
    
def letter_check(guess,d):
    if guess in d["Word"]:
        print("yes")
        
    else:
        print("no")
    