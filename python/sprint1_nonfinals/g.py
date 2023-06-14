def to_binary(number: int) -> str:
    m = ''
    while number > 1:
        if number % 2 == 1:
            i = 1
            m = str(i) + m
        else:
            i = 0
            m = str(i) + m
        number = number // 2
    m = str(number) + m
    return m


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
