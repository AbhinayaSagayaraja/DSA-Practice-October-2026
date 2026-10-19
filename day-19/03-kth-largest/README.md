# Kth Largest Element in Array

## Approach
Use Quickselect with partitioning to place a pivot in its
correct position. Continue searching only the region
containing the target index instead of sorting the array.

## Complexity
- Average Time: O(n)
- Worst-case Time: O(n^2)
- Auxiliary Space: O(1) iterative implementation.

## Edge Case
Invalid k values must be rejected.