from tasks.list_tasks.shopping_list import add_to_list


def test_reverse_list(new_list):
    add_to_list(new_list, "100")
    assert "100" in new_list
