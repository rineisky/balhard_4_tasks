from tasks.list_tasks.list_length import list_length


def test_list_length(new_list):
    assert list_length(new_list) == 10
