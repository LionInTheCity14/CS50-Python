from collections import defaultdict
def get_max_toys(s, k):
    hmap = defaultdict(int)
    l, res = 0, 0
    for r in range(len(s)):
        hmap[s[r]] += 1
        while l < r and len(hmap) > k:
            hmap[s[l]] -= 1
            if hmap[s[l]] == 0:   hmap.pop(s[l])
            l += 1
        if len(hmap) == k:
            res = max(res, r - l + 1)
    return res

s = 'abaccab'


print(get_max_toys(s, 2))