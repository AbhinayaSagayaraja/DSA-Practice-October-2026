def first_one(row):
    low = 0
    high = len(row) - 1
    answer = len(row)

    while low <= high:
        mid = low + (high - low) // 2

        if row[mid] == 1:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


def row_with_maximum_ones(matrix):
    max_ones = 0
    answer = -1

    for i in range(len(matrix)):
        position = first_one(matrix[i])

        ones = len(matrix[i]) - position

        if ones > max_ones:
            max_ones = ones
            answer = i

    return answer


matrix = [
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

print(row_with_maximum_ones(matrix))