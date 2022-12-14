Problem
--------

Given an Array[] of N elements and a number K. ( 1 <= K <= N ) .
Split the given array into K subarrays (they must cover all the elements).
The maximum subarray sum achievable out of K subarrays formed, must be the minimum possible. 
Find that possible subarray sum.

Problem Statement: https://www.geeksforgeeks.org/split-the-given-array-into-k-sub-arrays-such-that-maximum-sum-of-all-sub-arrays-is-minimum/

Example
-------
N=4 K=3
arr=[1,2,3,4]

Ans=2

N=9 K=6
arr=[5,10,10,2,1,7,8,9,5]

Ans=14

```python
def feasible(arr, subarr_sum, k) -> bool:
    current_subarr_sum = 0
    subarr_cnt = 0
    for ele in arr:
        # one edge case
        if ele > subarr_sum:
            return False

        current_subarr_sum += ele
        if current_subarr_sum > subarr_sum:
            current_subarr_sum = ele
            subarr_cnt += 1

    # last subarray after the previous one concluded
    subarr_cnt += 1
    print(subarr_cnt)
    return subarr_cnt <= k


def split_array(arr, n, k):
    start_sub_sum, end_sub_sum = max(arr), sum(arr)

    while start_sub_sum < end_sub_sum:
        mid_sum = start_sub_sum + (end_sub_sum - start_sub_sum) // 2
        if feasible(arr, mid_sum, k):
            end_sub_sum = mid_sum
        else:
            start_sub_sum = mid_sum + 1

    return end_sub_sum


if __name__ == '__main__':
    print(split_array([1, 2, 3, 4], 4, 3))
    print(split_array([1, 1, 2], 3, 2))
    print(split_array([5, 10, 10, 2, 1, 7, 8, 9, 5], 9, 6))
```

