def replace_elements_by_rank(arr: list[int]) -> list[int]:
    
    # Creating dummy list to store the sorted elements.
    dummy_arr = sorted(arr)
    my_dict = {}
    final_list = []
    
    # Assign a rank to every element using temp variable.
    temp = 1
    for i in dummy_arr:
        if i not in my_dict:
            my_dict[i] = temp
            temp += 1
        
    for i in arr:
        final_list.append(my_dict[i])
    
    return final_list


my_list = [20, 15, 26, 2, 98, 6]
result = replace_elements_by_rank(my_list)
print(result)