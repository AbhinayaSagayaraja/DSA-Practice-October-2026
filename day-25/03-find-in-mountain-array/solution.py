def find_peak(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2

        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low


def ascending_search(nums, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def descending_search(nums, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def find_in_mountain_array(nums, target):
    peak = find_peak(nums)

    # Search the increasing side first
    result = ascending_search(nums, target, 0, peak)

    if result != -1:
        return result

    # If not found, search the decreasing side
    return descending_search(
        nums, target, peak + 1, len(nums) - 1
    )


nums = [1, 3, 5, 7, 6, 4, 2]

print(find_in_mountain_array(nums, 4))
print(find_in_mountain_array(nums, 7))
print(find_in_mountain_array(nums, 8))