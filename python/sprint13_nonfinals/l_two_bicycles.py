def binarySearch(money, price, left, right):
    if (right <= left and left != 0):
        return -1
    mid = (left + right) // 2
    if (money[mid] >= price and (money[mid - 1] < price or mid == 0)):
        return mid + 1
    elif price <= money[mid]:
        return binarySearch(money, price, left, mid)
    else:
        return binarySearch(money, price, mid + 1, right)


def two_bicycles(accumulation, price):
    accumulation = list(map(int, accumulation.split(' ')))
    lenght = len(accumulation)
    day_one_bicycles = binarySearch(accumulation, price, 0, lenght)
    day_two_bicycles = binarySearch(accumulation, price*2, 0, lenght)
    print(day_one_bicycles, end=' ')
    print(day_two_bicycles)


if __name__ == '__main__':
    _ = input()
    accumulation = input()
    price = int(input())
    two_bicycles(accumulation, price)
