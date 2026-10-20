def sort_binary(nums):
    count0 = 0

    for num in nums:
        if num != 0 and num != 1:
            raise ValueError("Array can contain only 0 and 1")

        if num == 0:
            count0 += 1

    for i in range(len(nums)):
        if i < count0:
            nums[i] = 0
        else:
            nums[i] = 1

    return nums


nums = [1, 0, 1, 1, 0, 0, 1]
print(sort_binary(nums))