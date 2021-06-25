from tasks.set_tasks.copy_set import copy_set


def test_common_elements(new_set):
    result = copy_set(new_set)
    assert result is not new_set
