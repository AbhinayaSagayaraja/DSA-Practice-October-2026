
def frequency_sort(s):
    freq = {}
    # Count each character
    for ch in s:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1
    chars = []
    for ch in freq:
        chars.append(ch)

    n = len(chars)
    # Arrange characters by decreasing frequency
    for i in range(n):
        big = i
        for j in range(i + 1, n):
            if freq[chars[j]] > freq[chars[big]]:
                big = j

        temp = chars[i]
        chars[i] = chars[big]
        chars[big] = temp

    # Repeat each character w.r.t its frequency
    ans = ""

    for ch in chars:
        for i in range(freq[ch]):
            ans = ans + ch
            
    return ans

s = "tree"
print(frequency_sort(s))
