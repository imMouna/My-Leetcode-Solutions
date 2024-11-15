def two_sum(nums: list, target: int) -> int:
    my_dict = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in my_dict:
            return [my_dict[diff], i]
        my_dict[num] = i
    
    return[-1]

arr = [2, 7, 11, 15]
target = 9
result = two_sum(arr, target)
print(result)

