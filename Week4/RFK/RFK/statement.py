import random
def SelectSentence():
    with open("CSE-210-1\Week4\RFK\RFK\statements.txt","r") as f:
        Lines=f.read().splitlines()
        random_line=random.choice(Lines)
        return random_line