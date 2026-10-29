def insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)

    # Add intervals that finish before the new interval starts.
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge all intervals that overlap with the new interval.
    while i < n and intervals[i][0] <= new_interval[1]:
        if intervals[i][0] < new_interval[0]:
            new_interval[0] = intervals[i][0]

        if intervals[i][1] > new_interval[1]:
            new_interval[1] = intervals[i][1]

        i += 1

    result.append(new_interval)

    # Add the remaining intervals.
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]

print(insert_interval(intervals, new_interval))