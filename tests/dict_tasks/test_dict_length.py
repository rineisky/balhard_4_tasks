from tasks.dict_tasks.dict_length import products_num


def test_products_num(new_dict):
    assert products_num(new_dict) == 10
