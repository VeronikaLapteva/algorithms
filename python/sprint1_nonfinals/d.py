from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    k = 0
    if len(temperatures) == 1:
        return 1
    if temperatures[0] > temperatures[1]:
        k += 1
    for i in range(len(temperatures)-2):
        if temperatures[i] < temperatures[i+1] and temperatures[i+1] > temperatures[i+2]:
            k += 1
    if temperatures[len(temperatures)-1] > temperatures[len(temperatures)-2]:
        k += 1
    return k


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
