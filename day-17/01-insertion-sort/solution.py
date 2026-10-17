
def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i - 1

        # Shift bigger elements to the right
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1

        # Insert key in the correct position
        nums[j + 1] = key

    return nums


nums = [5, 2, 4, 1, 3]
print(insertion_sort(nums))
