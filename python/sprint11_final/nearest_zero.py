'''Ближайший ноль

Проверка решения
ID = 88154925'''


from typing import List


def neighbours_zero(house: List[int]) -> List[int]:
    zero_left = house.index(0)
    for index, element in enumerate(house):
        if element == 0:
            zero_left = index
        else:
            house[index] = abs(index-zero_left)
    house = house[::-1]
    zero_left = house.index(0)
    for index, element in enumerate(house):
        if element == 0:
            zero_left = index
        else:
            house[index] = min(abs(index-zero_left), element)
    house = house[::-1]
    return house


def read_input() -> List[int]:
    input()
    house = list(map(int, input().strip().split()))
    return house


house = read_input()
print(" ".join(map(str, neighbours_zero(house))))
