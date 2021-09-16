"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
В программе в словаре LOG хранятся логи доступа администраторов к сервису.

Написать функцию clear_dict, которая чистит логи

ПРИМЕРЫ
--------------------------------------------------------------------------------
clear_dict(LOG) -> {}
"""
log = {
    'bestAdminEver': '22.01.2021 - MOD: clients',
    'linuxxxoid': '20.01.2021 - MOD: partners',
    'perry23': '22.01.2021 - MOD: clients',
    'tryAgain': '22.01.2021 - MOD: price-list',
}


def clear_dict(log_dict: dict) -> dict:
    log_dict.clear()
    return log_dict


if __name__ == '__main__':
    print('Очистка лога LOG..')
    res_log = clear_dict(log)
    print('Операция прошла успешно!' if res_log is log and len(log) == 0 else 'Ошибка!')
