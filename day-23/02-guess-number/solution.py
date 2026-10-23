# Simulated API: replace this value to test other cases
picked_number = 6


def guess(num):
    if num > picked_number:
        return -1
    elif num < picked_number:
        return 1
    else:
        return 0


def guess_number(n):
    low = 1
    high = n

    while low <= high:
        mid = low + (high - low) // 2
        result = guess(mid)

        if result == 0:
            return mid
        elif result == -1:
            high = mid - 1
        else:
            low = mid + 1

    return -1


print(guess_number(10))