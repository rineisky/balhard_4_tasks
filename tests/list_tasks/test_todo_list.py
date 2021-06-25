from tasks.list_tasks.todo_list import add_by_index


def test_todo_list(new_list):
    add_by_index(new_list, 3, "new")
    assert "new" in new_list
    assert new_list[3] == "new"
