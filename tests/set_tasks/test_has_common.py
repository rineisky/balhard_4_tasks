from tasks.set_tasks.has_common import has_common


def test_has_common(new_set):
    assert has_common(new_set, {1, 2, 3})
    assert not has_common(new_set, {20, 30})
