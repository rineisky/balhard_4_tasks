from tasks.set_tasks.difference import diff


def test_diff(new_set):
    second_set = {2, 5, 7, 8, 9, 17}
    result = diff(new_set, second_set)
    assert result.isdisjoint(second_set)
    assert len(new_set) == 10
