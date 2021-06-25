from tasks.set_tasks.is_superset import is_superset


def test_is_superset(new_set):
    assert is_superset(new_set, {2, 3, 4})
    assert not is_superset(new_set, {20, 30})
    assert not is_superset(new_set, {8, 30})
