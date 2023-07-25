import random

def create_random_array(size):
    """
    Creates a random array of random numbers from the numbers 0 to size
    of user defined size
    
    Args:
        size: The size of the array to be made

    Returns:
        A randomly generated array of user defined size
    """
    array = list(range(0,size))
    random.shuffle(array)
    
    return array

def linear_search(array, number):
    """
    Very basic linear sort algorithum
    Args:
        array: A list of comparable elements to be sorted.
        number: The integer that is to be found.

    Returns:
        the count of the item in array or 
        returns -1 if there is no element found"""
    for i in array:
        counter += 1
        if i == number:
            return counter
    return -1


def bubble_sort(array):
    """
    Very basic bubble sort algorithum that 
        Args:
            array: A list of comparable elements to be sorted.

        Returns:
            A tuple containing the sorted array and the number of comparisons made during the sorting process.
    """
    comparison_count = 0
    # This number is used to prevent the algorithum from 
    # making comparrisons in the already sorted area of the array
    sorted_array_number = 0
    flag = True
    while flag:
        flag = False
        for i in range(len(array)-sorted_array_number-1):
            comparison_count += 1
            if array[i] > array[i+1]:
                flag = True
                temp_number = array[i]
                array[i] = array[i+1]
                array[i+1] = temp_number

    return array, comparison_count

def selection_sort(arr):
    """
    Sorts an array in ascending order using the Selection Sort algorithm.

    Args:
        arr: A list of comparable elements to be sorted.

    Returns:
        A tuple containing the sorted array and the number of comparisons made during the sorting process.

    """
    comparisons = 0
    n = len(arr)

    # Iterate through the entire array
    for i in range(n):
        # Find the index of the minimum element in the unsorted portion of the array
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first element in the unsorted portion of the array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Return the sorted array and the number of comparisons made during the sorting process
    return arr, comparisons

def quick_sort(arr):
    """
    Sorts an array in ascending order using the QuickSort algorithm.

    Args:
        arr: A list of comparable elements to be sorted.

    Returns:
        A tuple containing the sorted array and the number of comparisons made during the sorting process.

    """
    comparisons = 0
    n = len(arr)
    if n <= 1:
        # Base case: array is already sorted (or empty)
        return arr, comparisons

    # Select the last element in the array as the pivot
    pivot = arr.pop()

    # Partition the array into two sub-arrays: one containing elements less than the pivot
    # and another containing elements greater than or equal to the pivot
    left = []
    right = []
    for item in arr:
        comparisons += 1
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    # print("left", left)
    # print("right", right)
    # print("pivot", pivot)
    # print("comp", comparisons)

    # Recursively sort the sub-arrays
    left_sorted, left_comparisons = quick_sort(left)
    right_sorted, right_comparisons = quick_sort(right)
    # Combine the sorted sub-arrays with the pivot to get the final sorted array
    return left_sorted + [pivot] + right_sorted, comparisons + left_comparisons + right_comparisons