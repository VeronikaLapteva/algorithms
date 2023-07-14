'''Проверка решения ID = 88978381

Временную сложность алгоритма можно оценить в O(n log n).
Благодаря разделению списка на две части и рекурсивному вызову quick_sort для
каждой из частей, алгоритм выполнит log n рекурсивных вызовов сортировки.
Каждый из этих вызовов будет выполняться за O(n) времени,
так как внутри каждого вызова выполняется один проход по массиву,
что занимает O(n) времени.
Следовательно, общая временная сложность алгоритма будет O(n log n).

Пространственная сложность алгоритма составляет O(log(n)),
так как каждый вызов функции `quick_sort` использует дополнительные переменные
в стековом пространстве.
В худшем случае, когда каждый разделенный подсписок содержит только один
элемент, глубина рекурсии будет равна n, и пространственная сложность
будет O(n).
'''

import random


def quick_sort(competitors: list, left: int, right: int) -> int:
    if left >= right:
        return
    i, j = left, right
    pivot = competitors[random.randint(left, right)]
    while i <= j:
        while competitors[i] < pivot:
            i += 1
        while competitors[j] > pivot:
            j -= 1
        if i <= j:
            competitors[i], competitors[j] = competitors[j], competitors[i]
            i, j = i + 1, j - 1
    quick_sort(competitors, left, j)
    quick_sort(competitors, i, right)


def formating(competitors: list) -> list:
    return [- int(competitors[1]), int(competitors[2]), competitors[0]]


if __name__ == '__main__':
    n = int(input())
    competitors = list(formating(input().split()) for _ in range(n))
    quick_sort(competitors, left=0, right=len(competitors) - 1)
    print(*(list(zip(*competitors))[2]), sep="\n")
