import pytest

@pytest.fixture
def mocked_tk(mocker):
    mocked_tk = mocker.patch('mmdesigner.view.tk.Tk')
    return mocked_tk

@pytest.fixture
def mocked_tk_title(mocker):
    mocked_tk_title = mocker.patch('mmdesigner.view.tk.Tk.title')
    return mocked_tk_title
