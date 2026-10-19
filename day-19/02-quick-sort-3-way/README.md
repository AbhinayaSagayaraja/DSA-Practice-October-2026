# Quick Sort with 3-way Partition

## Approach
Partition the array into values smaller than, equal to, and
greater than the pivot. Recursively sort only the smaller
and greater regions.

## Complexity
- Average Time: O(n log n)
- Worst-case Time: O(n^2)
- Auxiliary Space: O(log n) average recursion stack;
  O(n) worst case.

## Edge Case
An array containing only equal values remains unchanged.