from tasks.set_tasks.sym_diff_update import sym_diff_update


def test_sym_diff_update(new_set):
    result = sym_diff_update(new_set, {3, 4, 6, 7, 8, 9, 10})
    assert result == {0, 1, 2, 5, 10}
    assert result is new_set
