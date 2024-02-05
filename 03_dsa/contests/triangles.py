def triangleType(nums) -> str:
    sum = 0
    mySet = set()

    for n in nums:
        mySet.add(n)
        sum += n
    
    for n in nums:
        if n >= sum - n:
            return 'none'
        
    l = len(mySet)
    if l == 1:
        return 'equilateral'
    elif l == 2:
        return 'isosceles' 
    else:
        return 'scalene'


print(triangleType([8,4,2]))
print(triangleType([5,3,8]))