# Implement inserstion sort
def insertionsort(arr):
    for index in range(1,len(arr)):
        curr_element = arr[index]
        pos = index
        while curr_element < arr[pos-1] and pos>0:
            arr[pos] = arr[pos-1]
            pos = pos-1
        arr[pos] = curr_element

l = [2,4,5,653,2,3345,7,3,23]
insertionsort(l)
print(l)
