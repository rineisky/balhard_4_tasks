"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая очистит множество
"""


def clear_set(collection: set) -> set:
    # TODO вставить код сюда
    collection.clear()
    return collection


if __name__ == '__main__':
    assert clear_set({1, 2, 3}) == set()
    print('Решено!')
