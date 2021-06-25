from tasks.dict_tasks.get_values import get_values


def test_get_values(new_dict):
    assert len(get_values(new_dict)) == 10
