def selection_sort(array):

    """ 
    Sorts an array using the selection sort algorithm. 

    This function implements the selection sort algorithm to sort the input array 
    in ascending order. It iterates through the array, finding the minimum element 
    in the unsorted portion and swapping it with the first unsorted element. 
 
    Args: 
        array (list): The input array to be sorted. 
 
    Returns: 
        list: The sorted array in ascending order. 
 
    Note: 
        This function modifies the input array in-place. 
    """ 

    for index in range(0, len(array)-1):
        value = array[index]
        current = index
        for element in range(index + 1, len(array)):
            if array[element] < array[current]:
                current = element
        array[index] = array[current]
        array[current] = value

    return array

unsorted_array = [8, 76, 32, 29, 58, 47, 13, 85, 503, 284, 143]

print(f' Unsorted array: {unsorted_array}')

selection_sort(unsorted_array)

print(f' Sorted array: {unsorted_array}')