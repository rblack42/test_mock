from mmdesigner.view import get_tkinter_root
from . Gui import Gui


def main(root):
    gui = Gui(root,500,400)
    gui.run()


# python -m mmdesigner
if __name__ == '__main__':
    root = get_tkinter_root()
    main(root)
