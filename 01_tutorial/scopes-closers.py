username = 'chaiaurcode'

def test():
    username = 'inside test()'
    a = 'a'
    print(username, a)

if True:
    username = 'inside if'
    print(username)

test()

print('global', username)


x = 99
# def func2(y):
#     # x = 9
#     z = x + y
#     return z

# print(func2(1))


# def func3():
#     global x    # most of the time you should avoid this
#     x = 12

# func3()

# def f1():
#     x = 88
#     def f2():
#         x = 12
#         print(x)
#     f2()
#     print(x)

# f1()
# print(x)


def f1():
    x = 88
    def f2():
        print(x)
    return f2

res = f1()
res()       # closers


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

res2 = chaicoder(2)
print(res2(5))

def curry(x):
    x = 75
    def curry2(y):
        return x + y
    return curry2

sum1 = curry(2)  # here sum1 gets curry2 reference along with x's binded value
sum2 = curry(5)  # that is 75, so 2 and 5 are going to use
print(sum1(15), sum2(25))   # 90, 100