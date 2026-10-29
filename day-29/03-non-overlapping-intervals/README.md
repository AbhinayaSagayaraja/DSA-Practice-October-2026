# Non-overlapping Intervals

## Approach
Sort intervals by their ending values. Keep the interval that ends earliest, and count a removal whenever the next interval overlaps with the last kept interval.

## Complexity
- Time: O(n log n), assuming an O(n log n) sorting algorithm.
- Auxiliary Space: O(1) excluding sorting space, depending on the sorting implementation.

## Edge Case
An empty interval list requires zero removals.