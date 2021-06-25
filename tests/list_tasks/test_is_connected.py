from tasks.list_tasks.is_connected import is_connected


def test_is_connected(new_list):
    assert is_connected(new_list, 2)
    assert not is_connected(new_list, 50)
