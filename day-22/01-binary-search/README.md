# Binary Search

## Approach
Maintain low and high pointers. Check the middle element
and discard half of the search range after each comparison.

## Complexity
- Time: O(log n)
- Auxiliary Space: O(1)

## Edge Case
An empty array returns -1.