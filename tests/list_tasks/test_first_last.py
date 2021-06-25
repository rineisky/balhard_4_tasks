from tasks.list_tasks.first_last import get_first_last


def test_get_first_last(new_list):
    first, last = get_first_last(new_list)
    assert first == 0
    assert last == 9
