
def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i - 1

        # Move larger elements one position right
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j = j - 1

        nums[j + 1] = key

    return nums


nums = [1, 2, 4, 3, 5, 6]
print(insertion_sort(nums))
