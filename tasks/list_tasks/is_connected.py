"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Есть список участников, которые подключились к конференции.

Написать функцию is_connected, которая проверяет, подключен ли некоторый пользователь
к конференции (вернуть True или False)

ПРИМЕРЫ
--------------------------------------------------------------------------------
is_connected('Андрей') -> True
is_connected('Олег') -> False
"""
from typing import Any

participants = ['Андрей', 'Ольга', 'Сергей', 'Виктор', 'Татьяна']


def is_connected(p_list: list, user: Any) -> bool:
    """
    Проверяет, есть ли user в p_list

    :param p_list: список участников
    :param user: пользователь
    :return: True или False
    """

    if participants in p_list:
        user = participants
    return user in p_list


if __name__ == '__main__':
    check_user = input('Введите имя участника для проверки: ').capitalize()
    print('Участник подключен'
          if is_connected(participants, check_user) else
          'Участник не подключен')
