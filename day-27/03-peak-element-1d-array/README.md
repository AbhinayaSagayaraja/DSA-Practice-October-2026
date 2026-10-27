# Peak Element in a 1D Array

## Approach
Use binary search to compare the middle element with
its right neighbour. Move toward the rising slope or
keep the middle element when the slope is falling.

## Complexity
- Time: O(log n)
- Auxiliary Space: O(1)

## Edge Case
An array containing only one element returns index 0.