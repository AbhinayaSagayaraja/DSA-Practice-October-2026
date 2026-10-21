# Sort Array by Increasing Frequency

## Approach
Count occurrences with a dictionary, then manually selection-sort
the unique values by increasing frequency. For equal frequencies,
place the larger value first. Rebuild the result from the counts.

## Complexity
- Time: O(n + u^2), where u is the number of unique values
- Auxiliary Space: O(n + u)

## Edge Case
If every value appears once, values are ordered descending.