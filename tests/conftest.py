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

@pytest.fixture
def mocked_tk_protocol(mocker):
    mocked_tk_protocol = mocker.patch('mmdesigner.view.tk.Tk.protocol')
    return mocked_tk_protocol

@pytest.fixture
def mocked_tk_destroy(mocker):
    mocked_tk_destroy = mocker.patch('mmdesigner.view.tk.Tk.destroy')
    return mocked_tk_destroy
