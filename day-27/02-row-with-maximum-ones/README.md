# Row with Maximum Ones

## Approach
Use binary search on every sorted row to find its first
1. Calculate the number of ones and track the row with
the maximum count.

## Complexity
- Time: O(m log n)
- Auxiliary Space: O(1)

## Edge Case
If every row contains only zeros, return -1.