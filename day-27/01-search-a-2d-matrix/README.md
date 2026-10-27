# Search a 2D Matrix

## Approach
Treat the matrix as a virtual 1D sorted array. Use binary
search and convert each middle index into a row and column
using integer division and modulo.

## Complexity
- Time: O(log(m * n))
- Auxiliary Space: O(1)

## Edge Case
The target does not exist in the matrix.