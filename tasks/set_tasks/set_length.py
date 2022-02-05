"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая возвращает длину множество
"""


def set_length(collection: set) -> int:
    collection = len(collection)
    result = collection
    return result


if __name__ == '__main__':
    assert set_length({1, 2, 3, 4}) == 4
    print('Решено!')
