"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Администратор подключает пользователя к системе хранения паролей.

Необходимо чтобы у пользователя были свои собственные пароли, а также чтобы
пользователь имел доступ к общим паролям.

(Изменить функцию copy_dict таким образом, чтобы она возвращала поверхностную
копию данных)
"""

TEST_TEMPLATE = {
    'a1': None,
    'a2': None,
    'a3': None,
    'b1': None,
    'b2': None,
    'b3': None,
    'c1': None,
    'd1': None,
}


def copy_dict(template: dict) -> dict:
    # TODO вставить код сюда
    template_copy = dict.copy(template)
    return template_copy


if __name__ == '__main__':
    print('Подготовка вашего теста...')
    test = copy_dict(TEST_TEMPLATE)
    print('Можете приступать к выполнению!'
          if test == TEST_TEMPLATE and test is not TEST_TEMPLATE else
          'Ошибка. Попробуйте позже...')
