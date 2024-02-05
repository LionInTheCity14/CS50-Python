def returnToBoundaryCount(nums) -> int:
    ant, cnt, n = 0, 0, len(nums)

    for i in range(n):
        ant += nums[i]

        if ant == 0:
            cnt += 1

    return cnt


print(returnToBoundaryCount([2,3,-5]))
print(returnToBoundaryCount([3,2,-3,-4]))