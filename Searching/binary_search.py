pos = -1
l = [1000,201201, 23, 45, 25, 12, 75, 32, 98, 32,56]

def binarySearch(arr, element):
    arr.sort()
    l = 0
    u = len(arr)
    while l <= u:
        mid = (l+u) // 2
        if arr[mid] == element:
            return mid
        else:
            if arr[mid] < element:
                l = mid
            else:
                u = mid

print(binarySearch(l,201201))

