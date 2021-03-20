import tkinter as tk

class Gui:

    WIDTH = 212
    HEIGHT = 104

    def __init__(self, root):
        self.root = root
        self.root.title("mmdesigner")
        self.root.geometry('{}x{}'.format(self.WIDTH, self.HEIGHT))
        self.protocol("WM_DELETE_WINDOW", self.close)
        print("gui initialized")

    def create_gui(self):

    def close(self):
        self.root.destroy()

def create_gui():
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", close
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    gui = Gui()
    gui.run()

