from tasks.list_tasks.clear_list import clear_list


def test_clear_list(new_list):
    result = clear_list(new_list)
    assert not result
    assert result is new_list
