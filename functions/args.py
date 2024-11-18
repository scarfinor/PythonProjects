# *args = parameter that will pack all arguments into a tuple so that a function can accept a varying amount of arguments.

def addExceptIndex0(*nums) :
    sum = 0
    nums = list(nums)
    nums[0] = 0
    for num in nums :
        sum += num
    return sum

print(addExceptIndex0(1, 2, 3, 4, 5, 6))