def main():
    x = int(input("What's x ? "))
    y = int(input("What's y ? "))
    sign = str(input("What's operation ? "))
    ans = None

    if sign == "power":
        ans = power(x, y)
    
    print(ans)


def power(x:int, y:int) -> int:
    return x ** y
 
main()