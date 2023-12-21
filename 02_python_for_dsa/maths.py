# division is decimal by default
print(5 / 2)     # 2.5

# double slash rounds down
print(5 // 2)    # 2

print(-5 / 2)   # -2.5

# CAREFUL : most languages rounds toward 0 by default but 
# python rounds dowm

print(-5 // 2)      # -3
print(int(-5 / 2))  # not it will round towards 0

# modding 
print(10 % 3)

# to be consistent with other languages modulo
print(-10 % 3)  # 2
import math
print(math.fmod(-10, 3))    # -1.0

# more math helpers

print(math.floor(3 / 2))    # 1
print(math.ceil(3 / 2))     # 2

print(math.sqrt(5))         # 2.2360...
print(math.pow(2, 3), 2 ** 3)   # 8.0, 8

# maximum and minimum integer
# for maximum -> float("inf")
# for minimum -> float("-inf")

# python numbers are infinite so they never overflow
print(float("-inf") < 2 ** -1000) # True
print(2 ** 1000 < float("inf")) # True
