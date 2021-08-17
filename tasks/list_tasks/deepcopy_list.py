"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Администратор подключает пользователя системе.

Имеется следующая структура данных [табельный номер, данные пользователя]

Пользователь создается по шаблону и должен иметь возможность редактировать
свои данные

(Нужно вернуть глубокую копию данных)
"""
user_data = {
    "name": None,
    "surname": None
}

user_template = [
    123456,
    user_data
]


def deepcopy_list(collection: list) -> list:
    # TODO вставить код сюда
    import copy
    collection_copy = copy.deepcopy(collection)
    return collection_copy


if __name__ == '__main__':
    print("Подключаем пользователя к системе...")
    user = deepcopy_list(user_template)
    if user is not user_template and user[1] is not user_data:
        print("Подключение прошло успешно!")
    else:
        print("Произошла ошибка при подключении...")
