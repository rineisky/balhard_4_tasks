"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая возвращает длину множество
"""


def set_length(collection: set) -> int:
    # TODO написать код ниже
    result = len(collection)
    return result


if __name__ == '__main__':
    assert set_length({1, 2, 3, 4}) == 4
    print('Решено!')
