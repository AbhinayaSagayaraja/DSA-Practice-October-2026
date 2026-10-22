# First Bad Version

## Approach
Binary-search versions from 1 to n. If the middle version is
bad, search the left half including mid; otherwise, search
the right half after mid.

## Complexity
- Time: O(log n)
- Auxiliary Space: O(1)

## Edge Case
The first version is already bad.