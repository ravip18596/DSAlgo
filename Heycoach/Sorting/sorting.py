def partition(arr, low, high):
    # Region 1: elements less than pivot
    # Region 2: elements greater than equal to pivot
    # Region 3: unexplored
    pivot = arr[high]
    i = low-1
    j = low
    while j <= high:
        if arr[j] >= pivot:
            j += 1 # increment region 2
        else:
            arr[i+1], arr[j] = arr[j], arr[i+1]
            i += 1 # increment region 1
            j += 1 # increment region 2

    # moving pivot to its correct position which is region 2 first element
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if low >= high:
        return

    pi = partition(arr, low, high)
    quick_sort(arr, low, pi - 1)
    quick_sort(arr, pi + 1, high)


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i-1
        temp = arr[i]
        while j>=0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

    arr = [10, 7, 8, 9, 1, 5]
    insertion_sort(arr)
    print(arr)

    arr = [10, 7, 8, 9, 1, 5]
    bubble_sort(arr)
    print(arr)

    arr = [10, 7, 8, 9, 1, 5]
    selection_sort(arr)
    print(arr)

    arr = [5,4,3,2,1]
    pivot = partition(arr, 0, len(arr) - 1)
    print(pivot)
    print(arr)

    arr = [1,2,3,4,5]
    pivot = partition(arr, 0, len(arr) - 1)
    print(pivot)
    print(arr)
