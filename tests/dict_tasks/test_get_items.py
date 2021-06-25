from tasks.dict_tasks.get_items import get_workers


def test_get_workers(new_dict):
    assert len(get_workers(new_dict)) == 10
