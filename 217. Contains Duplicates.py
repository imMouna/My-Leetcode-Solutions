def contains_duplicates(nums: list) -> bool:
    my_list = set()
    
    for i in nums:
        if i in my_list:
            return True
        my_list.add(i)
    
    return False

arr = [1, 2, 3, 3]
result = contains_duplicates(arr)
print(result)