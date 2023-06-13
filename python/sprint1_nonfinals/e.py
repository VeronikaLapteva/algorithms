def get_longest_word(line: str) -> str:
    lst = line.strip().split()
    result = max(lst, key=len)
    return result


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
