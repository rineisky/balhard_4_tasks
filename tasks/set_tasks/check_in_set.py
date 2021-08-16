"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая проверяет, есть ли элемент в множестве
Вернуть True или False
"""
from typing import Any


def check_in(collection: set, element: Any) -> bool:
    # TODO вставить код сюда
    result = element in collection
    return result


if __name__ == '__main__':
    assert check_in({1, 2, 3}, 2)
    assert not check_in({1, 2, 3}, 5)
    print('Решено!')
