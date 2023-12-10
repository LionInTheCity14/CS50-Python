x = float(input("what's x ? "))
y = float(input("what's y ? "))
sign = str(input("what's operation ? "))

z = None

if sign == '+':
    z = x + y
elif sign == '-':
    z = x - y
elif sign == '*':
    z = x * y
elif sign == '/':
    z = x / y
elif sign == "%":
    z = x % y
else:
    z = "Invalid sign"

z = round(z, 2)
print(f"{x} {sign} {y} = {z:,}")