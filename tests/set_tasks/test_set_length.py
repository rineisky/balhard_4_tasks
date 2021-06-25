from tasks.set_tasks.set_length import set_length


def test_set_length(new_set):
    assert set_length(new_set) == 10
