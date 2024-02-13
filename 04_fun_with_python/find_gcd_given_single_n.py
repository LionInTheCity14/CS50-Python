# gcd(n) = 2 ** (order // 2) - 1    # iff order is even

def find_gcd(B):
    order = find_order(B)
    if order < 0:   return
    one_factor = 2 ** (order / 2) - 1
    other_factor = 0
    if one_factor != 0:
        other_factor = B / one_factor
    return [one_factor, other_factor]

def find_order(B):
    if B == 0:
        return
    res = []
    seen = set()
    order, x = 0, 2

    for A in range(B + 1):
        val = (x ** A) % B
        if val in seen:
            order = A
            res.append(val) # to show repeatation
            break
        seen.add(val)
        res.append(val)

    print(f"for {B}, order is {order}")
    print(res)
    return order

n = int(input(f"What's the number ?? "))

print(f'gcd({n}) is comes out to be {find_gcd(n)}')
