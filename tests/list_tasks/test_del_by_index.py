from tasks.list_tasks.del_by_index import del_by_num


def test_del_by_num(new_list):
    result = del_by_num(new_list, 2)
    assert 1 not in result
