def counting_sort(nums):
    if len(nums) == 0:
        return nums

    minimum = nums[0]
    maximum = nums[0]

    for num in nums:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    counts = [0] * (maximum - minimum + 1)

    for num in nums:
        counts[num - minimum] += 1

    index = 0

    for i in range(len(counts)):
        while counts[i] > 0:
            nums[index] = i + minimum
            index += 1
            counts[i] -= 1

    return nums


nums = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(nums))