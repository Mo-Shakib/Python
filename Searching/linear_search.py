def linearSearch(arr, element): # array and element to find
    for i in arr:
        if i == element: 
            return arr.index(i) 
    return 'Element not found'

print(linearSearch([2,1,4,0,5],7))