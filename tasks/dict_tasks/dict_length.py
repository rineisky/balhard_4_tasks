"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Есть база с наименованиями товаров

Написать функцию products_num, которая возвращает количество наименований в базе

ПРИМЕРЫ
--------------------------------------------------------------------------------
products_num(PRODUCTS) -> 2
"""
PRODUCTS = {
    '112312': {
        'brand': 'Apple iPhone',
        'model': '11'
    },
    '774554': {
        'brand': 'Samsung',
        'model': 'Galaxy S10'
    },
}


def products_num(database: dict) -> int:
    # TODO написать код ниже
    result = len(database)
    return result


if __name__ == '__main__':
    print(f"Количество товаров в каталоге: {products_num(PRODUCTS)}")
