# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        for j in range (i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        if arr[cur_index] > arr[smallest_index]:
            old_cur = arr[cur_index]
            old_small = arr[smallest_index]
            arr[smallest_index] = old_cur
            arr[cur_index] = old_small

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range (0, len(arr)-1):
        for j in range (0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                old_i = arr[i]
                old_j = arr[j]
                arr[i] = old_j
                arr[j] = old_i


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr


