#import pytest
from mmdesigner.view import get_tkinter_root
from mmdesigner.Gui import Gui


def test_Tk_initialized(mocked_tk):
    root = get_tkinter_root()
    mocked_tk.assert_called_once()

def test_view_get_tkinter_root_sets_title(mocked_tk_title):
        get_tkinter_root()
        mocked_tk_title.assert_called_once()
        mocked_tk_title.assert_called_with("mmdesigner")

def test_constructor_sets_geometry(mocked_tk_geometry):
    root = get_tkinter_root()
    print("GEOM", type(root))
    gui = Gui(root, 500, 400)
    mocked_tk_geometry.assert_called_with("500x400")

def test_run_calls_mainloop(mocked_tk_mainloop):
    root = get_tkinter_root()
    print(type(root))
    print(dir(root))
    gui = Gui(root, 500, 400)
    gui.run()
    mocked_tk_mainloop.assert_called_once()



