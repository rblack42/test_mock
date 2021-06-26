from mmdesigner.view import get_tkinter_root

class Gui():

    def __init__(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height
        self.root.title('mmdesigner')
        self.root.geometry(f"{width}x{height}")

    def run(self):
        print("mmdesigner starting...")
        self.root.mainloop()

