"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию add_to_list, которая будет добавлять элементы, которые вводит
пользователь (передаются параметром в функцию), в список покупок

ПРИМЕРЫ
--------------------------------------------------------------------------------
add_to_list(shopping_list, 'молоко') -> ['молоко']
add_to_list(shopping_list, 'кефир') -> ['молоко', 'кефир']
add_to_list(shopping_list, 'яблоки') -> ['молоко', 'кефир', 'яблоки']
"""
shopping_list = []


def add_to_list(s_list: list, element: str) -> list:
    """
    Добавляет элемент 'element' в список 's_list'

    :param s_list: список покупок
    :param element: добавляемый продукт
    :return: список покупок
    """
    # TODO вставить код сюда
    s_list.append(element)
    return s_list


if __name__ == '__main__':
    print('Создаем список покупок. Для выхода введите \'exit\'')
    while True:
        new_element = input('Добавить товар: ')
        if new_element == 'exit':
            break
        add_to_list(shopping_list, new_element)
    print("\nНужно купить: \n" + ",\n".join(shopping_list))
