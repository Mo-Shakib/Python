def selection_sort(arr):
    for i in range(len(arr)): # first loop
        min_value = i # take i-th position as min value
        for j in range(i, len(arr)): # from i-th position to last position
            if arr[j] < arr[min_value]: # comparing min_value with others
                min_value = j # if the condition is True then the min value is j-th position
        
        temp = arr[i] # creating temporari variabe
        arr[i] = arr[min_value] # chinging the i-th value with the minimum value
        arr[min_value] = temp # swaping the value

    return arr # finally returning the sorted list
my_arr = [2,1,4,-4,6,8,5]
print(selection_sort(my_arr))

# Shakib, 15-Sep-2020; 02:57 AM


