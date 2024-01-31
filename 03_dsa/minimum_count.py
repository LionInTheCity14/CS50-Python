# import Counter from collections

word1 = "abcde"
word2 = "xyzxyzxyzxyz"
word3 = "aabbccddeeffgghhiiiiii"


def count(word):
    freq = [0] * 26
    for ch in word:
        freq[ord(ch) - ord('a')] += 1
    
    freq.sort(reverse=True)

    sum = 0
    for i in range(26):
        if i <= 7:
            sum += freq[i]
        elif i <= 15:
            sum += freq[i] * 2
        elif i <= 23:
            sum += freq[i] * 3
        else:
            sum += freq[i] * 4
    print(freq, sum)


# print(len(word1), count(word1))
# print(len(word2), count(word2))
print(len(word3), count(word3))
