"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
На сервере хранится лог запросов к серверу. Администратору необходимо знать,
сколько ошибок произошло за день.

Отредактировать функцию count_elements таким образом, чтобы с ее помощью
можно было посчитать количество элементов равных некоторому значению
"""
from typing import Any

TODAY_LOG = [
    "200 Success",
    "500 Error",
    "500 Error",
    "500 Error",
    "200 Success",
    "500 Error",
]


def count_elements(collection: list, element: Any) -> int:
    # TODO вставить код сюда
    count = collection.count(element)
    return count


if __name__ == '__main__':
    print(f"За сегодня произошло {count_elements(TODAY_LOG, '500 Error')} ошибок.")
