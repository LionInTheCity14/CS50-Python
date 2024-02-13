n1 = int(input("n1 "))
n2 = int(input("n2 "))
x = int(input('x '))

def check(n1, n2, x):
    if n1 >= n2 and x > 0:    return -1
    car1, car2 = x, 0
    cnt = 0
    while car2 <= car1:
        car1 += n1
        car2 += n2
        cnt += 1
    return cnt

print(check(n1, n2, x))