from tasks.dict_tasks.get_set import get_or_set


def test_get_or_set(new_dict):
    assert get_or_set(new_dict, 2) == 2
    assert get_or_set(new_dict, 20) == 3
    assert 20 in new_dict
