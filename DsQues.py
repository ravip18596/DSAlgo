def minimum_pizza_weight(arr,n):
    arr = sorted(arr)
    discard_len = n%4
    if discard_len > 0:
        n = n-discard_len
        arr = arr[:n]
    min_weight = 0
    #print(arr)
    for i in range(1,n,4):
        min_weight += arr[i]

    return min_weight


if __name__ == '__main__':
    n = int(input())
    arr = [0]*n
    for i in range(n):
        arr[i] = int(input())

    min_weight = minimum_pizza_weight(arr,n)
    print(min_weight)
