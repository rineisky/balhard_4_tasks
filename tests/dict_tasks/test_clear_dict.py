from tasks.dict_tasks.clear_dict import clear_dict


def test_clear_dict(new_dict):
    result = clear_dict(new_dict)
    assert result is new_dict
    assert len(result) == 0
