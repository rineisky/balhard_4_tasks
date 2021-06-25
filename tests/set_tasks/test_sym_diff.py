from tasks.set_tasks.sym_diff import sym_diff


def test_sym_diff(new_set):
    assert sym_diff(new_set, {3, 4, 6, 7, 8, 9, 10}) == {0, 1, 2, 5, 10}
