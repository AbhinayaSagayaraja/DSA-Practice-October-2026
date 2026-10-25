def peak_index_in_mountain_array(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2

        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low


nums = [0, 2, 5, 3, 1]
print(peak_index_in_mountain_array(nums))