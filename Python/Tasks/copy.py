def copy_sort(array):  # function defined for copy_sort
    
    copy = array[:]  # the array is assigned to copy
    sorted_copy = []  

    while len(copy) > 0: # constantly checks that the array length is greater than 0
        minimum = 0 # sets a minimum value
        for element in range(0, len(copy)): # generates integers from start number, 0, to stop number, array length
            if copy[element] < copy[minimum]: 
                minimum = element           # The function tries to find the smallest value in the list of numbers in each
                                            # loop. Once found, that value is subsequently removed and is "popped" (basically pasted)
                                            # in the new ordered list, which is assigned to sorted_copy.
                
        print('\tRemoving value', copy[minimum], 'from', copy)
        sorted_copy.append(copy.pop(minimum))
        
    return sorted_copy

array = [5, 3, 1, 2, 6, 4]   # array of numbers assigned

print('Copy Sort...\nArray:', array)

print('Copy:', copy_sort(array)) # copy_sort function called and returned. The list from sorted_copy is returned once all the
                                 # values are sorted.
print('Array:', array)     
