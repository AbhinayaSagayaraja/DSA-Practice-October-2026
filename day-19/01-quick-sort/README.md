# Quick Sort

## Approach
Implement Lomuto and Hoare partitioning. Partition the array
around a pivot, then recursively sort the remaining regions.

## Complexity
- Average Time: O(n log n)
- Worst-case Time: O(n^2)
- Auxiliary Space: O(log n) average recursion stack;
  O(n) worst case.

## Edge Case
An empty array requires no sorting.