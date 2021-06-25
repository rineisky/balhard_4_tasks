from tasks.list_tasks.first_3_last_3 import get_first_3_last_3


def test_get_first_3_last_3(new_list):
    first, last = get_first_3_last_3(new_list)
    assert first == [0, 1, 2]
    assert last == [7, 8, 9]
