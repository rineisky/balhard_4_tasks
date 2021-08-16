"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Отредактировать функцию month_to_season, которая принимает номер месяца,
таким образом, чтобы она возвращала название сезона, к которому относится
этот месяц

ПРИМЕРЫ
--------------------------------------------------------------------------------
- month_to_season(12) -> 'Зима'
- month_to_season(4) -> 'Весна'
- month_to_season(7) -> 'Лето'
- month_to_season(9) -> 'Осень'
"""
from collections import ChainMap


def month_to_season(month: int) -> str:
    Spring = {}.fromkeys([3, 4, 5], 'весна')
    Summer = {}.fromkeys([6, 7, 8], 'лето')
    Autumn = {}.fromkeys([9, 10, 11], 'осень')
    Winter = {}.fromkeys([12, 1, 2], 'зима')
    seasons = ChainMap(Spring, Summer, Autumn, Winter)
    season = seasons.get(month)
    return season


if __name__ == '__main__':
    month_number = int(input('Введите номер месяца: '))
    print(f'Сезон: {month_to_season(month_number)}')
