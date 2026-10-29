# Merge Intervals

## Approach
Sort intervals by their starting values. Traverse the sorted intervals and merge an interval with the previous one whenever they overlap. Otherwise, add it as a new interval.

## Complexity
- Time: O(n log n), assuming an O(n log n) sorting algorithm.
- Auxiliary Space: O(n) for the merged output, excluding sorting space.

## Edge Case
An empty input list should return an empty list.