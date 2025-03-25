def bubble_sort(unsorted):
    for n in range(len(unsorted) - 1, 0, -1):

        swap = False

        for i in range(n):

            if unsorted[i] > unsorted[i+1]:

                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
                swap = True

        if not swap:
            break

unsorted = [10,6,99,50,24,64,38,204,142]

print(unsorted)

bubble_sort(unsorted)

print(unsorted)