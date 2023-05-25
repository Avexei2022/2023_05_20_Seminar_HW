from random import randint


def my_map(func, list_items):
    list_items = list_items.copy()
    for i in range(0, len(list_items)):
        list_items[i] = func(list_items[i])
    return list_items


def print_result(list_old, list_new):
    print(*list_old, sep=', ', end=' -> ')
    print(*list_new, sep=', ')


list_num = [randint(1, 10) for i in range(10)]
list_map = map(lambda x: x * 10, list_num)
print_result(list_num, list_map)
list_my_map = my_map(lambda x: x * 10, list_num)
print_result(list_num, list_my_map)
