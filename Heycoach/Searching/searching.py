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


def findMin(nums: List[int]) -> int:
    if nums[0] <= nums[-1]:
        return nums[0]
    
    left, right = 1, len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] < nums[mid-1]:
            return nums[mid]
       
        if nums[mid] < nums[right]:
            right = mid-1
        else:
            left = mid+1


def search(nums: List[int], target: int) -> int:
        i, n = 1, len(nums)
        while i<n and nums[i-1]<nums[i]:
            i+=1

        pivot = i

        left, right = 0, n-1
        while left <= right:
            mid = (left+right)//2
            rotated_mid = (mid+pivot)%n
            if nums[rotated_mid] == target:
                return rotated_mid
            elif nums[rotated_mid] < target:
                left = mid+1
            else:
                right = mid-1

        return -1


if __name__ == "__main__":
    nums = [1,2,1,3,5,6,4]
    index = findPeakElement(nums)
    print(f"Peak element is at index {index} with value {nums[index]}")

    arr = [1,2,3,4,6,7,8,9]
    target = 5
    index = lower_bound(arr, target)
    print(f"Lower bound of {target} is at index {index} with value {arr[index]}")

    nums = [3,4,5,1,2]
    min_num = findMin(nums)
    print(f"Minimum number in the rotated sorted array is {min_num}")

    nums = [4,5,6,7,0,1,2]
    target = 0
    index = search(nums, target)
    print(f"Target {target} found at index {index}")
