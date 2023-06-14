'''Ловкость рук

Проверка решения
ID = 88169501'''

from collections import Counter
from typing import List, Tuple


def twist_wrist(row: str, k: int) -> int:
    qty_buttons: int = 2*k
    points: int = 0
    for value in Counter(row).values():
        if value <= qty_buttons:
            points += 1
    return points


def read_input(size_field: int = 4) -> Tuple[List[str], int]:
    k: int = int(input())
    line: list = []
    for i in range(size_field):
        line.append(input().replace('.', ''))
    row: str = ''.join(line)
    return row, k


if __name__ == '__main__':
    row, k = read_input()
    print(twist_wrist(row, k))
