
def selection_sort(nums):
    n = len(nums)

    for i in range(n):
        small = i

        # Find the smallest element in remaining array
        for j in range(i + 1, n):
            if nums[j] < nums[small]:
                small = j

        # Swap the smallest element into position i
        temp = nums[i]
        nums[i] = nums[small]
        nums[small] = temp

    return nums


nums = [5, 2, 4, 1, 3]
print(selection_sort(nums))
