from tasks.dict_tasks.get_keys import get_workers_names


def test_get_workers_names(new_dict):
    assert len(get_workers_names(new_dict)) == 10
