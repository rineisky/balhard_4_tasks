"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Есть база с пользователями users.

Написать функцию del_user, которая позволяет администратору по логину удалить
пользователя

ПРИМЕРЫ
--------------------------------------------------------------------------------
del_user('GroveGang') -> Пользователь успешно удален!
del_user('noWay') -> Пользователя с логином 'noWay' нет в системе!
"""
from typing import Any

users = {
    'hateSwimming': {
        'first_name': 'Tomy',
        'last_name': 'Vervetti',
        'age': 35
    },
    'GroveGang': {
        'first_name': 'Carl',
        'last_name': 'Johnson',
        'age': 24
    }
}


def del_user(users_dict: dict, login: Any) -> dict:
    # TODO вставить код сюда
    users_dict.pop(login)
    return login


if __name__ == '__main__':
    d_user = input('Введите логин для удаления: ')
    user_exist = d_user in users
    try:
        del_user(users, d_user)
    except KeyError:
        print(f"Пользователя с логином '{d_user}' нет в системе!")
    else:
        if d_user not in users and user_exist:
            print('Пользователь успешно удален!')
