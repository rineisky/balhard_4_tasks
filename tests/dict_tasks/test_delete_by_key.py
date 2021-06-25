from tasks.dict_tasks.del_by_key import del_user


def test_del_user(new_dict):
    del_user(new_dict, 1)
    del_user(new_dict, 5)
    assert 1 not in new_dict
    assert 5 not in new_dict
