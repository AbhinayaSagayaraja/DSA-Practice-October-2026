# Count Inversions in Array

## Approach
Use merge sort to count inversions within each half and across
the two halves. When a right-side element is smaller than the
current left-side element, count all remaining left-side elements.

## Complexity
- Time: O(n log n)
- Auxiliary Space: O(n)

## Edge Case
An already sorted array has zero inversions.