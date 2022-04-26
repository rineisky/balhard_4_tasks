"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая оставит в множестве только те элементы,
которые являются общими для него и другого множества
"""


def intersection_update(set_1: set, set_2: set) -> set:
    # TODO вставить код сюда
    set.intersection_update(set_1, set_2)
    return set_1


if __name__ == '__main__':
    some_set = {1, 2, 3, 4}
    intersection_update(some_set, {3, 4, 5})
    assert some_set == {3, 4}
    print('Решено!')
