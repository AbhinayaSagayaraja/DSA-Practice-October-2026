def is_perfect_square(num):
    if num < 0:
        return False

    low = 0
    high = num

    while low <= high:
        mid = low + (high - low) // 2

        if mid == 0:
            if num == 0:
                return True
            low = 1
            continue

        square = mid * mid

        if square == num:
            return True
        elif square < num:
            low = mid + 1
        else:
            high = mid - 1

    return False


print(is_perfect_square(16))
print(is_perfect_square(14))
print(is_perfect_square(0))