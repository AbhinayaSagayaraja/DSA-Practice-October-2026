# Find K Smallest Elements

### Approach
I use selection sort to bring the smallest elements to the beginning of the array. I repeat the process for the first k positions and copy those elements into the answer.

### Time Complexity
- Time: O(n × k)
- Auxiliary Space: O(k) for the answer list

### Edge Case
If k is 0 or negative, the answer should be an empty list.