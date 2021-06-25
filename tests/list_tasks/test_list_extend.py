from tasks.list_tasks.list_extend import list_extend


def test_list_extend(new_list):
    list_extend(new_list, [11, 12])
    assert 11 in new_list
    assert 12 in new_list
