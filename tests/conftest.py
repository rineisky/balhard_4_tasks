import pytest


@pytest.fixture()
def new_list():
    """Returns new list"""
    return [i for i in range(10)]


@pytest.fixture()
def new_set():
    """Returns new set"""
    return {i for i in range(10)}


@pytest.fixture()
def new_dict():
    """Returns new dict"""
    return {i: i for i in range(10)}
