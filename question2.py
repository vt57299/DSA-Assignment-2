# 2. Implement Merge Sort

def mergesort(arr):    
                                                # dividing orginal list
    if len(arr)>1:
        mid = len(arr)//2
        left_list = arr[:mid]
        right_list = arr[mid:]
        mergesort(left_list)
        mergesort(right_list)
         
        i,j,k = 0,0,0
        while i< len(left_list) and j< len(right_list):
            if left_list[i]< right_list[j]:
                arr[k] = left_list[i]
                i += 1
                k += 1
            else:
                arr[k] = right_list[j]
                j += 1
                k += 1

        # for remaining items
        while i< len(left_list):
            arr[k] = left_list[i]
            i +=1
            k +=1
        while j< len(right_list):
            arr[k] = right_list[j]
            j +=1
            k +=1

l = [9,8,3,1,7,56,2]
print("Original list: ",l)

mergesort(l)           # Calling sorting function
print("Sorted list: ",l)