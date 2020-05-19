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
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                sorted = False

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    count = [0 for x in range(len(arr))]
    #add correct counts
    for i in range (len(arr)):
        count[arr[i]] +=1
    print('first count', count)
    #sum them
    for i in range(1, len(count)):
        the_sum = count[i-1] + count[i]
        count[i] = the_sum

    print('second count', count)
    print('before last', arr)
    #put them in correct position
    temp_arr = [0 for x in range(len(arr))]
    for i in range(1, len(arr)+1):
        el = arr[len(arr)-i]
        index = count[el] - 1
        temp_arr[index] = el
        count[el] -= 1
        
    for i in range(len(arr)):
        arr[i] = temp_arr[i]
    return arr


# print(count_sort([3,2,1,3], 4))