my_list = [8, 4, 3, 9, 10, 2]


def insertion_sort(arr):
    '''
    Insertion sort function.
    O(n^2) complexity
    '''

    # Iterate starting at the second element
    for i in range(0, len(arr)-2):

        # Get the value we're working on, and start looking
        # immediately to the left
        curr_val = arr[i]
        check_ind = i-1

        # Move higher values to the right as long as
        # the value we're working on is lower
        while check_ind >= 0 and curr_val < arr[check_ind]:
            arr[check_ind + 1] = arr[check_ind]
            check_ind -= 1

        # Put the value we're working on in the lowest
        # position that met the 'while' criteria; + 1 is
        # because check_ind was already incremented
        arr[check_ind + 1] = curr_val

    return arr


def selection_sort(arr):
    '''
    Selection sort function.
    O(n^2) complexity
    '''

    # Iterate over the entire array
    for i in range(len(arr)):

        # Start with the current value, check each value to its right,
        # and if it's lower that the value in the current minimum_index
        # position, update the min_index with the new lower index
        min_index = i
        for x in range(i+1, len(arr)):
            if arr[x] < arr[min_index]:
                min_index = x

        # Swap the current index and the minimum value; vacuous
        # if min_index and i are the same
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def bubble_sort(arr):
    '''
    Bubble sort function.
    O(n^2) complexity
    '''

    # Loop over starting indices for pairs;
    # no pair start for the highest index
    for i in range(len(arr)):

        # Inner loop to compare pairs beginning with starting
        # index and then to the right of that
        for x in range(0, len(arr) - 1 - i):

            # Check each pair, and if out of order, fix
            if arr[x + 1] < arr[x]:
                arr[x + 1], arr[x] = arr[x], arr[x + 1]

    return arr
