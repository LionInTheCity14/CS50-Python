# print 1 to n
n = int(input("What's n ? "))
def oneToN(n):
    if n <= 0:
        return
    else:
        print(n, " ", end="")
        oneToN(n-1)

# print n to 1
def nToOne(n):
    if n <= 0:
        return
    else:
        nToOne(n - 1)
        print(n," ", end="")

oneToN(n)
print()
nToOne(n)
print()
    