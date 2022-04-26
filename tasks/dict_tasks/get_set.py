"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая возвращает значение по ключу, если ключа нет, то
создает ключ со значением 3 и возвращает его

Нельзя использовать if
"""
from typing import Any


def get_or_set(collection: dict, key: Any) -> Any:
    # TODO вставить код сюда
    result = collection.setdefault(key, 3)
    return result


if __name__ == '__main__':
    some_dict = {1: 100, 2: 200}
    assert get_or_set(some_dict, 2) == 200
    assert get_or_set(some_dict, 3) == 3
    print('Решено!')
