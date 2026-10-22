def first_bad_version(n, first_bad):
    low = 1
    high = n

    while low < high:
        mid = low + (high - low) // 2

        # Simulated is_bad_version API
        if mid >= first_bad:
            high = mid
        else:
            low = mid + 1

    return low


n = 5
first_bad = 4

print(first_bad_version(n, first_bad))