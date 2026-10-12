
def longest_subarray(nums, k):
    l = 0
    s = 0
    ans = 0

    for r in range(len(nums)):
        s += nums[r]  # add current num

        while s > k:
            s -= nums[l]  # remove left num
            l += 1

        if s == k:
            ans = max(ans, r - l + 1)  # longest length

    return ans


nums = [1, 2, 1, 1, 1, 3]
k = 3

print(longest_subarray(nums, k))
