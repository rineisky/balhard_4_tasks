"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернут развернутый список
"""
from copy import deepcopy


def reverse_list(collection: list) -> list:
    collection_copy = deepcopy(collection)
    collection_copy.reverse()
    return collection_copy


if __name__ == '__main__':
    assert [1, 2, 3] == reverse_list([3, 2, 1])
    print('Решено!')
