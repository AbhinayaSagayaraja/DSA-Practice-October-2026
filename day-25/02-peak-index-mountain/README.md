# Peak Index in a Mountain Array

## Approach
Use binary search to determine whether the slope is rising
or falling. Narrow the range until the peak index remains.

## Complexity
- Time: O(log n)
- Auxiliary Space: O(1)

## Edge Case
The peak may be near either end of the array.