import pytest

@pytest.fixture
def mocked_tk(mocker):
    mocked_tk = mocker.patch('mmdesigner.view.tk.Tk')
    return mocked_tk

@pytest.fixture
def mocked_tk_title(mocker):
    mocked_tk_title = mocker.patch('mmdesigner.view.tk.Tk.title')
    return mocked_tk_title

@pytest.fixture
def mocked_tk_geometry(mocker):
    mocked_tk_geometry = mocker.patch('mmdesigner.view.tk.Tk.geometry')
    return mocked_tk_geometry

@pytest.fixture
def mocked_tk_mainloop(mocker):
    mocked_tk_mainloop = mocker.patch('mmdesigner.view.tk.Tk.mainloop')
    return mocked_tk_mainloop
