def my_sqrt(x):
    if x < 2:
        return x

    low = 1
    high = x
    answer = 0

    while low <= high:
        mid = low + (high - low) // 2

        if mid <= x // mid:
            answer = mid
            low = mid + 1
        else:
            high = mid - 1

    return answer


print(my_sqrt(8))
print(my_sqrt(16))
print(my_sqrt(0))