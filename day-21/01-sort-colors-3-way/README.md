# Sort Colors — 3-way Partition

## Approach
Use low, mid, and high pointers to divide the array into
regions containing 0s, 1s, and 2s. Swap values into their
correct regions in one pass.

## Complexity
- Time: O(n)
- Auxiliary Space: O(1)

## Edge Case
An empty array requires no changes.