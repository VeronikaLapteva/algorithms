'''Проверка решения ID = 88943853

Временная сложность данного алгоритма составляет O(log n).
Каждый раз размер пространства поиска уменьшается вдвое.
В худшем случае, когда массив полностью упорядочен и не поврежден,
алгоритм будет выполняться за O(log n) времени.

Пространственная сложность данного алгоритма составляет O(1),
так как он использует только фиксированное количество дополнительной памяти
для хранения значений индексов и переменных.
'''
from typing import List


def broken_search(nums: List[int], target: int) -> int:

    left, right = 0, len(nums) - 1

    while left <= right:
        med = (left + right) // 2
        element_med = nums[med]
        if element_med == target:
            return med
        if nums[left] <= element_med:
            if nums[left] <= target < element_med:
                right = med - 1
            else:
                left = med + 1
        else:
            if element_med < target <= nums[right]:
                left = med + 1
            else:
                right = med - 1
    return -1


if __name__ == '__main__':
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
