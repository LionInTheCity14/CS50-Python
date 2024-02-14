from collections import Counter
from math import inf

def find_minimum_window(s, t):
    l, res = 0, [-1, -1]
    size = inf
    tmap = Counter(t)
    cnt = len(tmap)
    for r in range(len(s)):
        if s[r] in tmap:
            tmap[s[r]] -= 1
            if tmap[s[r]] == 0: cnt -= 1

        while l < r and (s[l] not in tmap or tmap[s[l]] < 0):
            if s[l] in tmap:    tmap[s[l]] += 1
            l += 1
        
        if cnt == 0 and (r - l + 1) < size:
            size = r - l + 1
            res[0], res[1] = l, r
    
    return s[res[0] : res[1] + 1]

s = 'ababdbefcafab'
t = 'aabc'
print(find_minimum_window(s, t))