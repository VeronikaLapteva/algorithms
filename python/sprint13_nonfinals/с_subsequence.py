'''Нужно понять, является ли первая из них подпоследовательностью второй.'''


def subsequence(substring, whole_line):
    if len(substring) == 0:
        return True
    position = -1
    for i in substring:
        position = whole_line.find(i, position + 1)
        if position == - 1:
            return False
    return True


if __name__ == '__main__':
    print(subsequence(input(), input()))
