def count_inversions(nums):
    def sort_and_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_count = sort_and_count(arr[:mid])
        right, right_count = sort_and_count(arr[mid:])

        merged = []
        i = 0
        j = 0
        cross_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                cross_count += len(left) - i
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        total = left_count + right_count + cross_count
        return merged, total

    _, count = sort_and_count(nums)
    return count


nums = [2, 4, 1, 3, 5]
print(count_inversions(nums))