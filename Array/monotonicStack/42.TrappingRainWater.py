from typing import List

def trap(height: List[int]) -> int:
    # water += min(max_left, max_right) - arr[i]
    # Space: O(1)
    # Time: O(N)      
    lmax, rmax = 0, 0
    left, right = 0, len(height)-1
    water = 0
    while left < right:
        lmax = max(lmax, height[left])
        rmax = max(rmax, height[right])

        if lmax < rmax:
            water += lmax - height[left]
            left += 1
        else:
            water += rmax - height[right]
            right -= 1

    return water


def trap2(height):
    # water += min(max_left, max_right) - arr[i]
    # Space: O(N)
    # Time: O(N)
    water = 0
    n = len(height)
    right = [0]*n
    right[n-1] = height[n-1]
    for i in range(n-2,-1,-1):
        right[i] = max(height[i], right[i+1])

    max_left = 0
    for i in range(n):
        max_left = max(max_left, height[i])
        water += min(max_left, right[i]) - height[i]

    return water
