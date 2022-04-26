"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Дан список покупок в приложении. Предоставить пользователю возможность удалять
товар по его названию
"""
shopping_list = ["молоко", "сметана", "сыр"]


def del_by_value(collection: list, value: str) -> list:
    # TODO вставить код сюда
    collection.remove(value)
    return collection


if __name__ == '__main__':
    print("Удаляем: сметана...")
    result = del_by_value(shopping_list, "сметана")
    if "сметана" not in shopping_list:
        print("Удаление прошло успешно!")
    else:
        print("Произошла ошибка при удалении...")
