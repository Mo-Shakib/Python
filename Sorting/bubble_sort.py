l = [5,3,1,9,8,2,4,7]

def BubbleSort(array):
    for i in range(len(array)-1,0,-1): # counting the loop
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j] # store array[j] into a temp variable
                array[j] = array[j+1] # swap the value
                array[j+1] = temp
    return array
print(BubbleSort(l))




