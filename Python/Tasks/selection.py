def selection_sort(array):

    # This outer loop will start to store each element's value
    # and current index number from the input, which is a
    # list reference.
    
    for index in range(0, len(array) - 1):
        value = array[index]
        current = index

        # Inner loop executes main algorithm by where the smallest unsorted
        # value is swapped with the first unsorted value each time.

        for element in range(index + 1, len(array)):
            if array[element] < array[current]:
                current = element

        array[index] = array[current]
        array[current] = value
        print('\tResolving element [', index, '] to', array)

# Declared list as array and display the unsorted array.

array = [5, 3, 1, 2, 6, 4]
print('Selection Sort...\nArray :', array)

# Call the function selection_sort and display the output of the function,
# which is the sorted list.

selection_sort(array)
print('Array: ', array)
