# Guess Number Higher or Lower

## Approach
Use binary search over versions from 1 to n. Use the
guess API response to discard half the search range.

## Complexity
- Time: O(log n)
- Auxiliary Space: O(1)

## Edge Case
The picked number is 1 or n.