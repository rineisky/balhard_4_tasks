from tasks.dict_tasks.check_in_dict import check_in


def test_check_in(new_dict):
    assert check_in(new_dict, 2)
    assert not check_in(new_dict, 500)
