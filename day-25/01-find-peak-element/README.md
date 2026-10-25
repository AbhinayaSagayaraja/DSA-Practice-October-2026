# Find Peak Element

## Approach
Use binary search to compare the middle element with its
right neighbor. Move toward the rising slope until a peak
index is found.

## Complexity
- Time: O(log n)
- Auxiliary Space: O(1)

## Edge Case
An array with one element returns index 0.