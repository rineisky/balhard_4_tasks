"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Есть словарь USERS:

- ключи - логины пользователей
- значения - данные пользователей

Пользователь вводит свой логин.

Написать функцию check_in, которая проверяет, есть ли данный логин в системе (USERS).
Вернуть True или False

ПРИМЕРЫ
--------------------------------------------------------------------------------
check_in('no_way') -> False
check_in('GroveGang') -> True
"""
from typing import Any

USERS = {
    'hateSwimming': {
        'first_name': 'Tomy',
        'last_name': 'Vercetti',
        'age': 35
    },
    'GroveGang': {
        'first_name': 'Carl',
        'last_name': 'Johnson',
        'age': 24
    }
}


def check_in(users: dict, key: Any) -> bool:
    # TODO вставить код сюда
    result = key in users
    return result


if __name__ == '__main__':
    login = input('Введите login: ')
    print(f"Логин '{login}' "
          f"{'есть' if check_in(USERS, login) else 'не найден'} в системе")
