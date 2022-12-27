"""
Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.
Input:
N = 9, K = 3
arr[] = 1 2 3 1 4 5 2 3 6
Output: 
3 3 4 5 5 5 6 
Explanation: 
1st contiguous subarray = {1 2 3} Max = 3
2nd contiguous subarray = {2 3 1} Max = 3
3rd contiguous subarray = {3 1 4} Max = 4
4th contiguous subarray = {1 4 5} Max = 5
5th contiguous subarray = {4 5 2} Max = 5
6th contiguous subarray = {5 2 3} Max = 5
7th contiguous subarray = {2 3 6} Max = 6
"""

def max_of_subarrays(arr,n,k):
    max_so_far = 0
    for i in range(k):
        max_so_far = max(max_so_far, arr[i])
    
    result = [max_so_far]
    i = 1
    while i<=n-k:
        if max_so_far == arr[i-1]:
            # if prev ele in sliding window is the greatest element then whole window max
            max_so_far = max(arr[i:i+k])
        
        if max_so_far < arr[i+k-1]:
            # if new ele added in sliding window is greater than last max
            max_so_far = arr[i+k-1]
    
    
        result.append(max_so_far)
        i += 1
    
    return result