
def min_subarray_len(target, nums):
    l = 0
    s = 0
    ans = float("inf")

    for r in range(len(nums)):
        s += nums[r]  # add current num

        while s >= target:
            n = r - l + 1  # window length
            ans = min(ans, n)  # keep shortest

            s -= nums[l]  # remove left num
            l += 1  # move left

    if ans == float("inf"):
        return 0

    return ans


target = 7
nums = [2, 3, 1, 2, 4, 3]

print(min_subarray_len(target, nums))
