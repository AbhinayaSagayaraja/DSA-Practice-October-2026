def sort_colors(nums):
    count0 = 0
    count1 = 0
    count2 = 0

    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        elif num == 2:
            count2 += 1
        else:
            raise ValueError("Array can contain only 0, 1, and 2")

    index = 0

    for _ in range(count0):
        nums[index] = 0
        index += 1

    for _ in range(count1):
        nums[index] = 1
        index += 1

    for _ in range(count2):
        nums[index] = 2
        index += 1

    return nums


nums = [2, 0, 2, 1, 1, 0]
print(sort_colors(nums))