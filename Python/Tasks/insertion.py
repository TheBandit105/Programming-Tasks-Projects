def insertion_sort(array):
    for index in range(1, len(array)):
        value = array[index]

        while array[index - 1] > value and index >= 1:
            array[index] = array[index - 1]
            index -= 1
            array[index] = value

    print('\tResolving element [', index, '] to ', array)

array = [5, 3, 1, 2, 6, 4]
print('Insertion Sort... \nArray: ', array)

insertion_sort(array)
print('Array: ', array)
