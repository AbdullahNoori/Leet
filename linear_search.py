def linear_search(list, target):
    """Returns the index position of the target if found, else returns None"""
    
    for i in range(0, len(list)):
        if list[i]==target:
            return i 
        
    return None
    


#Test function 
def verify(index):
    if index is not None:
        print("Target Found at index: ", index)
    else: 
        print("Target not found in list")
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result is not found 
result = linear_search(numbers, 12)
verify(result)
# result is found
result = linear_search(numbers, 6)
verify(result)