import random
def change_window(root):
    win_width=int(random.randint(1000,2000))
    win_height=int(random.randint(500,1000))
    root.geometry(f"{win_width}x{win_height}")
    return win_width,win_height