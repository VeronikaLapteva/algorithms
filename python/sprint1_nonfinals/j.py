from typing import List
import math


def factorize(number: int) -> List[int]:
    fact = []
    for i in range(2, int(math.sqrt(number))+1):
        while number % i == 0:
            number = number // i
            fact.append(i)
    if number != 1:
        fact.append(number)
    return fact


result = factorize(int(input()))
print(" ".join(map(str, result)))
