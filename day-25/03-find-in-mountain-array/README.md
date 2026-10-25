# Find in Mountain Array

## Approach
First find the mountain peak using binary search. Search
the increasing side, then search the decreasing side if
the target was not found.

## Complexity
- Time: O(log n)
- Auxiliary Space: O(1)

## Edge Case
The target is absent from the mountain array.