"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая возвращает True, множество содержится в другом, и
False, если нет

Не использовать if
"""


def is_subset(set_1: set, set_2: set) -> bool:
    # TODO вставить код сюда
    result = set_1.issubset(set_2)
    return result


if __name__ == '__main__':
    assert is_subset({1, 2}, {1, 2, 3, 4})
    assert not is_subset({1, 2}, {5, 6, 3, 4})
    print('Решено!')
