
def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

    return nums


nums = [5, 2, 4, 1, 3]
print(bubble_sort(nums))
