def merge_sort(array):
    if len(array) > 1:
        middle = int(len(array)/2)
        left = array[0 : middle]; right = array[middle :]
        print('\tSplit to', left, right)

        merge_sort(left); merge_sort(right)

        i = j = 0
        for element in range(len(array)):
            L = left[i]if i < len(left) else None
            R = right[j]if j < len(right) else None
            if((L and R) and (L < R)) or R is None:
                array[element] = L; i += 1
            elif((L and R) and (L >= R)) or L is None:
                array[element] = R; j += 1
        print('\t\tMerging', left, right)

array = [5, 3, 1, 2, 6, 4]
print('Merge Sort... \nArray: ', array)

merge_sort(array)
print('Array: ', array)
            
