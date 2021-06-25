from tasks.set_tasks.clear_set import clear_set


def test_check_in(new_set):
    result = clear_set(new_set)
    assert result is new_set
    assert len(new_set) == 0
