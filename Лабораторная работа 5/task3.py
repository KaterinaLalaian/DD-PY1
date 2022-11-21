from random import randint


def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_) < 15:  # TODO написать функцию для получения списка уникальных целых чисел
        a = randint(-10, 10)
        if a not in list_:
            list_.append(a)
        if len(list_) >= 15:
            break
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
