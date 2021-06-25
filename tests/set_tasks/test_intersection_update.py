from tasks.set_tasks.intersection_update import intersection_update


def test_intersection_update(new_set):
    result = intersection_update(new_set, {2, 5, 7, 8, 9, 17})
    assert result is new_set
    assert result == {2, 5, 7, 8, 9}
