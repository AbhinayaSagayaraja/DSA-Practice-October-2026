# 3Sum

## Approach
Sort the array using merge sort. Fix one number and use two pointers to find pairs that make the total sum zero. Skip duplicate values to avoid repeated triplets.

## Complexity
- Time: O(n²)
- Auxiliary Space: O(n log n) for merge sort, excluding the output list.

## Edge Case
An array with fewer than three elements should return an empty list.