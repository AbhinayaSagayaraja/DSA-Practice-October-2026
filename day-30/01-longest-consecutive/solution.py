def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def longest_consecutive(nums):
    if len(nums) == 0:
        return 0

    nums = merge_sort(nums)

    longest = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue

        if nums[i] == nums[i - 1] + 1:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current

    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))