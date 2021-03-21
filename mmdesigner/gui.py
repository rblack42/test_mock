from tkinter import Tk

class Gui:

    WIDTH = 212
    HEIGHT = 104

    def __init__(self):
        self.root = Tk()
        self.root.title("mmdesigner")
        self.root.geometry('{}x{}'.format(self.WIDTH, self.HEIGHT))
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        print("gui initialized")
        self.root.mainloop()

    def close(self):
        print("gui terminated")
        self.root.destroy()


if __name__ == '__main__':
    Gui()

