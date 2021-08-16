"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет только элементы двух множеств кроме общих
"""


def sym_diff(set_1: set, set_2: set) -> set:
    # TODO вставить код сюда
    result = set_1.symmetric_difference(set_2)
    return result


if __name__ == '__main__':
    some_set = {1, 2, 3, 4}
    another_set = {3, 4, 5}
    assert sym_diff(some_set, another_set) == {1, 2, 5}
    assert some_set == {1, 2, 3, 4}
    assert another_set == {3, 4, 5}
    print('Решено!')
