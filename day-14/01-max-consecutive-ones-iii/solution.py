
def longest_ones(nums, k):
    l = 0
    zeros = 0
    ans = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            zeros += 1  # count zero

        while zeros > k:
            if nums[l] == 0:
                zeros -= 1  # remove zero
            l += 1

        ans = max(ans, r - l + 1)  # longest window

    return ans


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longest_ones(nums, k))
