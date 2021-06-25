from tasks.list_tasks.deepcopy_list import deepcopy_list


def test_deepcopy_list(new_list):
    mutable = {}
    new_list.append(mutable)
    result = deepcopy_list(new_list)
    assert result is not new_list
    assert result[-1] is not mutable
