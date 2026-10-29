# Insert Interval

## Approach
Traverse the sorted intervals and first add those that end before the new interval begins. Merge overlapping intervals into the new interval, then append the remaining intervals.

## Complexity
- Time: O(n)
- Auxiliary Space: O(n) for the result list.

## Edge Case
The new interval may overlap every existing interval.