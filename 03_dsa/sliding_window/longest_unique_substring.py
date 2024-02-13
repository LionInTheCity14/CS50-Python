from collections import defaultdict
def get_longest(s, k):
    l, res = 0, 0
    hmap = defaultdict(int)
    for r in range(len(s)):
        hmap[s[r]] += 1
        while l < r and len(hmap) > k:
            hmap[s[l]] -= 1
            if hmap[s[l]] == 0: hmap.pop(s[l])
            l += 1
        if len(hmap) == k:
            res = max(res, r - l + 1)
    return res

s = 'aabacbebebeebc'
print(get_longest(s, 3))
