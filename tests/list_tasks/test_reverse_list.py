from tasks.list_tasks.reverse_list import reverse_list


def test_reverse_list(new_list):
    assert reverse_list(new_list) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
