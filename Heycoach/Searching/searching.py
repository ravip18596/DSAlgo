from typing import List


def findPeakElement(nums: List[int]) -> int:
    """
    Time complexity: O(log n)
    """
    n = len(nums)
    if n==1:
        return 0

    if nums[0] > nums[1]:
        return 0
    if nums[n-1] > nums[n-2]:
        return n-1

    l, r = 1, n-2
    while l<=r:
        mid = (l+r)>>1
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid

        if nums[mid] < nums[mid+1]:
            l = mid+1
        else:
            r = mid-1


def lower_bound(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


if __name__ == "__main__":
    nums = [1,2,1,3,5,6,4]
    index = findPeakElement(nums)
    print(f"Peak element is at index {index} with value {nums[index]}")

    arr = [1,2,3,4,6,7,8,9]
    target = 5
    index = lower_bound(arr, target)
    print(f"Lower bound of {target} is at index {index} with value {arr[index]}")
