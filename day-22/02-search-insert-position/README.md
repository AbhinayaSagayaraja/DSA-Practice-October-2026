# Search Insert Position

## Approach
Use binary search to find the target. If it is absent,
return low, which identifies its insertion position.

## Complexity
- Time: O(log n)
- Auxiliary Space: O(1)

## Edge Case
The target is smaller than every array element.