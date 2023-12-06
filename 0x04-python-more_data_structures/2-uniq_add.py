#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    sum_unique = 0
    
    for num in my_list:
        if num not in unique_set:  # Check if the number is not already in the set
            sum_unique += num     # Add the unique number to the sum
            unique_set.add(num)   # Add the unique number to the set
    
    return sum_unique
