# Two Sum II - Input Array Is Sorted

## Approach
Use two pointers at opposite ends of the sorted array. Move the left pointer forward when the sum is too small and the right pointer backward when the sum is too large. Return the matching indices using 1-based indexing.

## Complexity
- Time: O(n)
- Auxiliary Space: O(1)

## Edge Case
The two numbers that form the target may be at the beginning and end of the array.