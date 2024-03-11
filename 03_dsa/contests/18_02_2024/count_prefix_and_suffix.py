words1 = ["a","aba","ababa","aa"]
words2 = ["pa","papa","ma","mama"]
from collections import List
def countPrefixSuffixPairs(words: List[str]) -> int:
    def is_prefix_and_suffix(s1, s2):
        
        pass
    
    cnt = 0
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:  continue
            cnt += is_prefix_and_suffix(words[i], words[j])
    return cnt
