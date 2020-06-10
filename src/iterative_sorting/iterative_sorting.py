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
# def count_sort(arr, maximum=-1):
#     # Your code here
#     count = [0 for x in range(len(arr))]
#     #add correct counts
#     hasNegatives = False
#     if len(arr) > 0:
#         for i in range (len(arr)):
#             if arr[i] > 0:
#                 count[arr[i]] +=1
#             else:
#                 hasNegatives = True
#         if hasNegatives == False:
#             #sum them
#             for i in range(1, len(count)):
#                 the_sum = count[i-1] + count[i]
#                 count[i] = the_sum
#             #put them in correct position
#             temp_arr = [0 for x in range(len(arr)+1)]
#             for i in range(1, len(arr)+1):
#                 el = arr[len(arr)-i]
#                 index = count[el] - 1
#                 temp_arr[index] = el
#                 count[el] -= 1
                
#             for i in range(len(arr)):
#                 arr[i] = temp_arr[i]
#             return arr
#     elif len(arr) == 0:
#         return arr
#     else:
#         return "Error, negative numbers not allowed in Count Sort"


# print(count_sort([3,2,1,3], 4))

def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr
    
    #if maximum is not given, we'll take the max value from the input array
    if maximum == -1:
        maximum = max(arr)

    #make a bunch of buckets (add one to include max value)
    #underscore is common when not actually using the iterator
    buckets = [0 for _ in range(maximum+1)]

    for x in arr:
        if x < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[x] += 1

    #loop through our buckets, starting at the smallest index
    j=0
    for i in range(len(buckets)):
        while buckets[i] > 0:
            arr[j] = i
            j+=1
            buckets[i] -=1

    return arr