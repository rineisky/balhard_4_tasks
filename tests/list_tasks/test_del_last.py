from tasks.list_tasks.del_last import del_last


def test_del_last(new_list):
    last_val = new_list[-1]
    deleted = del_last(new_list)
    assert last_val == deleted
    assert last_val not in new_list
