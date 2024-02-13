from math import *
from collections import *
def count_anagrams(s, p):
    pSize,sSize = len(p), len(s)
    if pSize > sSize:   return
    freq = Counter(p)
    l, cnt = 0, len(freq)
    res = 0
    for r in range(sSize):
        if s[r] in freq:
            freq[s[r]] -= 1
            if freq[s[r]] == 0:    cnt -= 1
        
        if r - l + 1 == pSize:
            if cnt == 0:    res += 1
            if s[l] in freq:
                freq[s[l]] += 1
                if freq[s[l]] == 1:   cnt += 1
            l += 1
    return res

s = 'abcbaewbcab'
p = 'abcb'
print(count_anagrams(s, p))