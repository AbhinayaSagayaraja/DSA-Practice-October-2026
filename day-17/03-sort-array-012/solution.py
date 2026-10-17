
def sort012(nums):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i - 1

        # Insert the current value in the right position
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1

        nums[j + 1] = key

    return nums


nums = [2, 0, 1, 2, 1, 0]
print(sort012(nums))
