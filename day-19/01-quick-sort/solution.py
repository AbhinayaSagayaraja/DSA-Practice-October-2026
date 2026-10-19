# Lomuto partition
def lomuto_partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


def quick_sort_lomuto(nums, low, high):
    if low < high:
        pivot_index = lomuto_partition(nums, low, high)
        quick_sort_lomuto(nums, low, pivot_index - 1)
        quick_sort_lomuto(nums, pivot_index + 1, high)


# Hoare partition
def hoare_partition(nums, low, high):
    pivot = nums[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort_hoare(nums, low, high):
    if low < high:
        split = hoare_partition(nums, low, high)
        quick_sort_hoare(nums, low, split)
        quick_sort_hoare(nums, split + 1, high)


nums1 = [8, 3, 1, 7, 0, 10, 2]
quick_sort_lomuto(nums1, 0, len(nums1) - 1)
print("Lomuto:", nums1)

nums2 = [8, 3, 1, 7, 0, 10, 2]
quick_sort_hoare(nums2, 0, len(nums2) - 1)
print("Hoare:", nums2)