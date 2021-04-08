import tkinter as tk
from . gui import Gui


def main(root):
    gui = Gui(root)
    gui.run()


# python -m mmdesigner
if __name__ == '__main__':
    root = tk.Tk()
    main(root)
