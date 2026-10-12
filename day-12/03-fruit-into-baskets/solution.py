
def total_fruits(fruits):
    l = 0
    count = {}
    ans = 0

    for r in range(len(fruits)):
        f = fruits[r]
        count[f] = count.get(f, 0) + 1  # add fruit

        while len(count) > 2:
            old = fruits[l]
            count[old] -= 1  # remove left fruit

            if count[old] == 0:
                del count[old]  # remove fruit type

            l += 1

        ans = max(ans, r - l + 1)  # longest window

    return ans


fruits = [1, 2, 1, 2, 3]
print(total_fruits(fruits))
