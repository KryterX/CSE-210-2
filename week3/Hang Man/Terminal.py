



def setup(d):
    word=d["Word"]
    for x in range(len(word)):
        temp= d["lab1"].cget("text")
        d["lab1"].config(text=f"{temp} _")