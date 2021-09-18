"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая получает 2 списка и возвращает все уникальные элементы
из этих двух списков
"""


def common_elements(list_1: list, list_2) -> set:
    list_1 = set(list_1)
    list_2 = set(list_2)
    result = list_1.union(list_2)
    return result


if __name__ == '__main__':
    assert common_elements([1, 2, 3], [2, 3, 4]) == {1, 2, 3, 4}
    print('Решено!')
