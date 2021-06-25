from tasks.list_tasks.del_by_value import del_by_value


def test_del_by_value(new_list):
    result = del_by_value(new_list, 2)  # noqa
    assert 2 not in result
