arr1, arr2 = [1,10,100], [1000]
arr3, arr4 = [1,2,3], [4,4,4]

def find_longest(s1, s2):
    cnt = 0
    n = len(s1) if len(s1) < len(s2) else len(s2)
    i = 0
    while i < n:
        if s1[i] != s2[i]:  break
        cnt += 1
        i += 1
    return cnt

def longestCommonPrefix(arr1, arr2) -> int:
    res = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            res = max(res, find_longest(str(arr1[i]), str(arr2[j])))
    return res

# print(find_longest("100", "1000"))
print(longestCommonPrefix(arr3, arr2))