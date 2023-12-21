# if statements don't need parentheses or curly braces

n = 1
if n > 2:
    print("greater")
elif n == 2:
    print("equal")
else:
    print("less")

# parentheses needed for multi-line conditions.
# and == &&
# or == ||
    
n, m = 3, 2
if((n > 2 and
   n != m) or n == m):
    print(n, m)
