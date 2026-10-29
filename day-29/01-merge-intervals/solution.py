def merge_intervals(intervals):
    if len(intervals) == 0:
        return []

    # Sort intervals by their starting value.
    # Replace this with your own merge sort for the challenge.
    intervals = sorted(intervals, key=lambda interval: interval[0])

    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        current = intervals[i]
        last = merged[-1]

        if current[0] <= last[1]:
            # The intervals overlap, so extend the end.
            if current[1] > last[1]:
                last[1] = current[1]
        else:
            merged.append(current)

    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))