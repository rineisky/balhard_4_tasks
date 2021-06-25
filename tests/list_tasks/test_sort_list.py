from tasks.list_tasks.sort_list import sort_list


def test_sort_list(new_list):
    new_list.insert(3, 20)
    new_list.insert(5, -20)
    asc, desc = sort_list(new_list)
    assert asc[0] == -20
    assert asc[-1] == 20
    assert desc[0] == 20
    assert desc[-1] == -20
