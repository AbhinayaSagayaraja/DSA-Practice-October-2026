# Insertion Sort on Nearly-Sorted Array

### Approach
I use insertion sort to place each element in its correct position. Since the array is already almost sorted, only a few elements may need to shift.

### Time Complexity
- Time: O(n) for an already sorted array; O(n²) in the worst case
- Auxiliary Space: O(1)

### Edge Case
An already sorted array should remain unchanged.