from tasks.set_tasks.union import get_union


def test_get_union(new_set):
    assert get_union(new_set, {3, 4, 6, 7, 8, 9, 10}) == {
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    }
