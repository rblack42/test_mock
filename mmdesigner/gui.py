from mmdesigner.view import get_tkinter_root

class Gui():

    def __init__(self, root):
        self.root = root
        self.root.title('mmdesigner')

    def run(self):
        print("mmdesigner starting...")
        self.root.mainloop()

