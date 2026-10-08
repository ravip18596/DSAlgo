# Selection Sort

def findMinIndex(arr, i):
    min_idx = i
    for k in range(i, len(arr)):
        if arr[min_idx] >= arr[k]:
            min_idx = k

    return min_idx

def selection_sort(arr):
    for i in range(len(arr)):
        j = findMinIndex(arr, i)
        # swap
        arr[i], arr[j] = arr[j], arr[i]

    return arr
    

if __name__ == '__main__':
    print(selection_sort([5,3,1,4,2]))