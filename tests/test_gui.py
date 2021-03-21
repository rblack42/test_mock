import pytest
import gui


class TestGui:

    def test_tk_Initialized(self, mocker):
        mock_main = mocker.MagicMock()
        mocker.patch("gui.Tk.mainloop", mock_main)
        gui.Gui()
        mock_main.assert_called()
