def minimumTimeToInitialState(word, k) -> int:
    def palindrome():
        i, j = 0, n - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True
    
    n = len(word)
    if not palindrome():
        return int(n / k)
    
    word1 = word
    

print(minimumTimeToInitialState('abacaba', 3))
print(minimumTimeToInitialState('abacaba', 4))
print(minimumTimeToInitialState('abcbabcd', 2))
print(minimumTimeToInitialState('aa', 1))
