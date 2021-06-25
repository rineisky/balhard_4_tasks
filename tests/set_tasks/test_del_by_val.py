from tasks.set_tasks.del_by_val import del_by_value


def test_del_by_value(new_set):
    del_by_value(new_set, 6)
    assert 6 not in new_set
