heights1 = [0,1,0,2,1,0,1,3,2,1,2,1]    # 6
heights2 = [4,2,0,3,2,5]                # 9
heights3 = [3, 5, 0, 1, 2, 4]           # 9
#           0, 1, 2, 3, 4, 5
# ngl      [0, 3, 3, 3, 0, 4]
# ngr      [4, 1, 3, 4, 0, 0]
# area     [9, ]

def two_pointers(heights):
    l, r = 0, len(heights) - 1
    maxL, maxR = heights[l], heights[r]
    water = 0
    while l < r:
        if maxL < maxR:
            l += 1
            maxL = max(maxL, heights[l])
            water += maxL - heights[l]
        else:
            r -= 1
            maxR = max(maxR, heights[r])
            water += maxR - heights[r]
    return water

print(two_pointers(heights1))
print(two_pointers(heights2))
print(two_pointers(heights3))