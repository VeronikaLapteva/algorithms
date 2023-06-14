from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    number_list = int(''.join(map(str, number_list)))
    res = number_list + k
    sum_list = []
    for i in str(res):
        sum_list.append(i)
    return sum_list


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
