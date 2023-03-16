# Implement Binary search

def binarysearch(arr,value):
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if value == arr[mid]:
            print("Value font at index: ",mid)
            break
        elif value > arr[mid]:
            low = mid+1
        else:
            high = mid-1
    else:
        print("Value not found")

l = [1,4,6,32,56,2,7,9,3]
# l.sort()
# print(l)

val = 43
binarysearch(l,val)