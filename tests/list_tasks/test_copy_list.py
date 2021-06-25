from tasks.list_tasks.copy_list import copy_list


def test_copy_list(new_list):
    mutable = {}
    new_list.append(mutable)
    result = copy_list(new_list)
    assert result is not new_list
    assert result[-1] is mutable
