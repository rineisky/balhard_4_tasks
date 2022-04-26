"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Администратор подключает пользователя системе.

Имеется следующая структура данных [имя, фамилия, данные департамента]

Пользователь должен иметь возможность редактировать свои фамилию и имя, а
данные департамента регулируются администратором

(Нужно вернуть поверхностную копию данных)
"""
department = {
    "name": "IT",
    "head": "Marina"
}

user_data_template = [
    "Не указано",
    "Не указано",
    department
]


def copy_list(collection: list) -> list:
    # TODO вставить код сюда
    collection_copy = collection.copy()
    return collection_copy


if __name__ == '__main__':
    print("Подключаем пользователя к системе...")
    user_data = copy_list(user_data_template)
    if user_data is not user_data_template and user_data[2] is department:
        print("Подключение прошло успешно!")
    else:
        print("Произошла ошибка при подключении...")
