from tasks.set_tasks.unique_in_list import get_unique_in_list


def test_get_unique_in_list():
    assert get_unique_in_list([1, 2, 1, 3, 2]) == {1, 2, 3}
