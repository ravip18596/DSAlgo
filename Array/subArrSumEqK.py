def subArraySum(arr, n, s): 
    #Write your code here
    # Time: O(n)
    # Space: O(1)
    if sum(arr) == s:
        return [1,n]

    cnt = {}
    cnt[0] = 0
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        if current_sum - s in cnt.keys():
            index = cnt[current_sum-s]
            return [index+1, i+1]
            #cnt[current_sum-s] = (prev[0]+1, i)

        cnt[current_sum] = i+1

def brute_force(arr, n, s):
    # Time - O(n^2)
    # Space - O(n)
    prefix_sum = [0]*(n+1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

    i = 0
    while i<n:
        for j in range(i, n):
            range_sum = prefix_sum[j+1] - prefix_sum[i]
            print(i,j,range_sum)
            if range_sum == s:
                return [i+1, j+1]
        i+=1

    return [-1]
    
if __name__ == '__main__':
    arr = [28, 68, 142, 130, 41, 14, 175, 2, 78, 16, 84, 14, 193, 25, 2, 193, 160, 71, 29, 28, 85, 76, 187, 99, 171, 88, 48, 5, 104, 22, 64, 107, 164, 11, 
172, 90, 41, 165, 143, 20, 114, 192, 105, 19, 33, 151, 6, 176, 140, 104, 23, 99, 48, 185, 49, 172, 65]
    result = subArraySum(arr, 57, 1562)
    result2 = brute_force(arr, 57, 1562)
    print(result, result2)

    result = subArraySum([1,2,3,4,5,6,7,8,9,10], 10, 54)
    result2 = brute_force([1,2,3,4,5,6,7,8,9,10], 10, 54)
    print(result, result2)