
def longest_substring(s):
    l = 0
    seen = set()
    ans = 0

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])  # remove repeated char
            l += 1

        seen.add(s[r])  # add current char
        ans = max(ans, r - l + 1)

    return ans


s = "abcabcbb"
print(longest_substring(s))
