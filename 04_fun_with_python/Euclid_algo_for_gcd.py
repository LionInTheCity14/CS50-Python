a = int(input(f"What's the number a ?? "))
b = int(input(f"What's the number b ?? "))

def find_euclid_gcd(a, b):
    if a == 0:  return b
    return find_euclid_gcd(b % a, a)

print(f"gcd({a, b}) is {find_euclid_gcd(a, b)}")