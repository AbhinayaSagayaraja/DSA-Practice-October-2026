
def k_smallest(nums, k):
    n = len(nums)

    if k <= 0:
        return []

    if k > n:
        k = n

    # Place the smallest element in each of the first k positions
    for i in range(k):
        small = i

        for j in range(i + 1, n):
            if nums[j] < nums[small]:
                small = j

        temp = nums[i]
        nums[i] = nums[small]
        nums[small] = temp

    # Copy the first k elements into the answer
    ans = []

    for i in range(k):
        ans.append(nums[i])

    return ans


nums = [7, 2, 9, 1, 5]
k = 3
print(k_smallest(nums, k))
