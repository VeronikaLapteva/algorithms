def is_power_of_four(number: int) -> bool:
    while number > 1:
        if number % 4 != 0:
            return False
        else:
            number = number // 4
            if number == 1:
                return True
    if number == 1:
        return True


print(is_power_of_four(int(input())))
