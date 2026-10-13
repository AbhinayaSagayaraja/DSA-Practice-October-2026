def contains_nearby_duplicate(nums, k):
    seen = {}

    for i in range(len(nums)):
        x = nums[i]

        if x in seen and i - seen[x] <= k:
            return True  # close enough duplicate

        seen[x] = i  # save latest index

    return False


nums = [1, 2, 3, 1]
k = 3

print(contains_nearby_duplicate(nums, k))
