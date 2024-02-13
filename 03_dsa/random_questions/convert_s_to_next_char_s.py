s = 'ransoHSAEGDFK dEAHOC'

def convert_string(s: str) -> str:
    if len(s) <= 0: return 'Invalid Input'
    res = []
    for ch in s:
        if not ch.isalpha() or ch == 'z' or ch == 'Z':
            continue
        else:
            res.append(chr(ord(ch) + 1))
    return ''.join(res)

print(convert_string(s))