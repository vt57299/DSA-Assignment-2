# implement Quick sort


def pivot_place(arr,first,last):           
    pivot = arr[first]
    left = first + 1
    right = last
    while True:
        while left <= right and arr[left] <= pivot:
            left = left +1         
        while left <= right and arr[right] >= pivot:
            right = right -1
        if right < left:
            break
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[first],arr[right] = arr[right],arr[first]
    return right

def quicksort(arr,first,last):
    if first < last:
        p = pivot_place(arr,first,last)
        quicksort(arr,first,p-1)
        quicksort(arr,p+1,last)

# main
l = [3,5,334,65,1,4,76,2]

n = len(l)
quicksort(l,0,n-1)

print(l)
