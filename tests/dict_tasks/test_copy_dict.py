from tasks.dict_tasks.copy_dict import copy_dict


def test_copy_dict(new_dict):
    result = copy_dict(new_dict)
    assert result is not new_dict
