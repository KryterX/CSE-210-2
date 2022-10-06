from tkinter import messagebox
import change
import setup
def reset(root,d):
    messagebox.showinfo(title="",message="You found the cat!!")
    width, height =change.change_window(root)
    setup.config_grid(width,height,d,root)