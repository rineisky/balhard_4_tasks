from tasks.set_tasks.update_set import update_set


def test_update_set(new_set):
    result = update_set(new_set, {1, 2, -2, 12})
    assert result is new_set
    assert result == {-2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12}
