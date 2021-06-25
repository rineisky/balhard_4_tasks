from tasks.list_tasks.count_element import count_elements


def test_count_elements(new_list):
    new_list.append(1)
    new_list.insert(2, 1)
    assert count_elements(new_list, 1) == 3
    assert count_elements(new_list, 100) == 0
