def frequency_sort(nums):
    freq = {}

    # Count each number manually
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    # Collect unique values
    values = []
    for num in freq:
        values.append(num)

    # Selection sort: lower frequency first;
    # for ties, larger value first
    n = len(values)

    for i in range(n - 1):
        best = i

        for j in range(i + 1, n):
            a = values[j]
            b = values[best]

            if freq[a] < freq[b] or (
                freq[a] == freq[b] and a > b
            ):
                best = j

        values[i], values[best] = values[best], values[i]

    # Rebuild the result using the frequencies
    result = []

    for num in values:
        for _ in range(freq[num]):
            result.append(num)

    return result


nums = [1, 1, 2, 2, 2, 3]
print(frequency_sort(nums))