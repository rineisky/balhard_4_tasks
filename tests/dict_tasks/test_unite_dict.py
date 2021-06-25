from tasks.dict_tasks.unite_dict import unite_dict


def test_unite_dict(new_dict):
    result = unite_dict(new_dict, {12: 12})
    assert 12 in result
    assert result is new_dict
