# Sort Characters By Frequency

### Approach
I count how often each character appears using a dictionary. Then I arrange the characters by frequency using a manual selection-style scan and repeat each character according to its count.

### Time Complexity
- Time: O(n²) for the manual frequency-ordering approach
- Auxiliary Space: O(n)

### Edge Case
If the input string is empty, the result should also be an empty string.