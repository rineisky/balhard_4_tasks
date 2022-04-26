"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Пользователь вводит некоторую работу и вводит индекс, куда надо вставить работу

Написать функцию add_by_index, которая добавляет работу на
указанную позицию в список дел

ПРИМЕРЫ
--------------------------------------------------------------------------------
add_by_index(todo_list, 0, 'Купить продукты') -> ['Купить продукты']
add_by_index(todo_list, 1, 'Вынести мусор') -> ['Купить продукты', 'Вынести мусор']
add_by_index(todo_list, 1, 'Приготовить поесть') -> ['Купить продукты', 'Приготовить поесть', 'Вынести мусор']
add_by_index(todo_list, 0, 'Сделать зарядку') -> ['Сделать зарядку', 'Купить продукты', 'Приготовить поесть', 'Вынести мусор']
"""
todo_list = []


def add_by_index(td_list: list, index: int, element: str) -> list:
    """
    Добавляет element в ed_list по индексу index

    :param td_list: список дел
    :param index: индекс задачи
    :param element: задача
    :return: список дел
    """
    # TODO вставить код сюда
    td_list.insert(index, element)
    return td_list


if __name__ == '__main__':
    print('Создаем список покупок. Для выхода введите \'exit\'')
    while True:
        new_element = input('Введите работу: ')
        if new_element == 'exit':
            break
        new_index = input('На какое место вставить: ')
        if new_index == 'exit':
            break
        add_by_index(todo_list, int(new_index), new_element)
    print("\nСписок дел:")
    for item_num, item in enumerate(todo_list, start=1):
        print(f"{item_num}. {item}")
