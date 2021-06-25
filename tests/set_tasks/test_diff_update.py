from tasks.set_tasks.diff_update import diff_update


def test_diff_update(new_set):
    result = diff_update(new_set, {2, 5, 7, 8, 9, 17})
    assert result is new_set
    assert result == {0, 1, 3, 4, 6}
