"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет те элементы,
которые есть во всех множествах
"""


def get_union(set_1: set, set_2: set) -> set:
    # TODO вставить код сюда
    result = set_1.union(set_2)
    return result


if __name__ == '__main__':
    some_set = {1, 2, 3, 4}
    another_set = {3, 4, 5}
    assert get_union(some_set, another_set) == {1, 2, 3, 4, 5}
    assert some_set == {1, 2, 3, 4}
    assert another_set == {3, 4, 5}
    print('Решено!')
