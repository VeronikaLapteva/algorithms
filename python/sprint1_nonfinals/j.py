from typing import List

def factorize(number: int) -> List[int]:
    l = [2,3,5,7,9]
    for i in l:
        while number % i == 0:
            number = number // i
            



result = factorize(int(input()))
print(" ".join(map(str, result)))
