from tkinter import *
from tkinter.messagebox import *
import sys
from notepad import config

class Help():
    def about(root):
        showinfo(title="About", message=f"This a simple text editor implemented in Python's Tkinter | Made by {config.name}")


def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    helpMenu.add_command(label="About", command=help.about)
    menubar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'main.py'")
