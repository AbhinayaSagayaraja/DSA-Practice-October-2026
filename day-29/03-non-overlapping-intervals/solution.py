def erase_overlap_intervals(intervals):
    n = len(intervals)

    if n == 0:
        return 0

    # Sort by ending value.
    # Replace this with your own merge sort for the challenge.
    intervals = sorted(intervals, key=lambda interval: interval[1])

    removals = 0
    last_end = intervals[0][1]

    for i in range(1, n):
        if intervals[i][0] < last_end:
            # Overlap: remove this interval.
            removals += 1
        else:
            # No overlap: keep this interval.
            last_end = intervals[i][1]

    return removals


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(erase_overlap_intervals(intervals))