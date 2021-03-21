import pytest
from mmdesigner import gui


class TestGui:

    def test_tk_Initialized(self, mocker):
        mock_main = mocker.MagicMock()
        mocker.patch("mmdesigner.gui.Tk.mainloop", mock_main)
        gui.Gui()
        mock_main.assert_called()
