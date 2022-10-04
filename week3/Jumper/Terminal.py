import Director



def setup(d):
    word=d["Word"]
    for x in range(len(word)):
        temp= d["lab2"].cget("text")
        d["lab2"].config(text=f"{temp} _")
    Director.Setup(d)