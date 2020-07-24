"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    # Your code goes here
    max = len(input_array)-1
    min = 0
    mid = (max+min)//2
    while (min<=max):        
        if (value==input_array[mid]):
            return mid
        elif (value<input_array[mid]):
            max= mid-1
        else:
            min = mid+1
        mid = (max+min)//2
    return -1
