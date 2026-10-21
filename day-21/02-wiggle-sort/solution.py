def wiggle_sort(nums):
    for i in range(len(nums) - 1):
        if i % 2 == 0:
            # Even index: nums[i] <= nums[i + 1]
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        else:
            # Odd index: nums[i] >= nums[i + 1]
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums


nums = [3, 5, 2, 1, 6, 4]
print(wiggle_sort(nums))