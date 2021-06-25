#import pytest
from mmdesigner.view import get_tkinter_root

def test_Tk_initialized(mocked_tk):
    root = get_tkinter_root()
    mocked_tk.assert_called_once()

def test_view_get_tkinter_root_sets_title(mocked_tk_title):
        get_tkinter_root()
        mocked_tk_title.assert_called_once()
        mocked_tk_title.assert_called_with("mmdesigner")



