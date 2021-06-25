from tasks.set_tasks.is_subset import is_subset


def test_is_subset(new_set):
    assert is_subset({2, 3, 4}, new_set)
    assert not is_subset({20, 30}, new_set)
    assert not is_subset({8, 30}, new_set)
