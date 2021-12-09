"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
В базе хранится список сотрудников.

Реализовать функцию list_extend, которая позволит при найме добавлять список
новых сотрудников к текущему
"""
user_list = [
    "Антон Петров",
    "Алла Ивановна"
]

new_workers = [
    "Иван Сергеев",
    "Артем Викторович"
]


def list_extend(first_list: list, second_list: list) -> list:
    first_list = first_list.extend(second_list)
    return first_list


if __name__ == '__main__':
    print(f"В компании работает {len(user_list)} человек.")
    print(f"В компании пришло {len(new_workers)} человека: {', '.join(new_workers)}")
    list_extend(user_list, new_workers)
    print(f"Теперь компании работает {len(user_list)} человек.")
