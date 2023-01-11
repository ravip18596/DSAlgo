# Problem
Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.

Example 1:

Input: n = 6 
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
Output: 3
Explanation: 
Minimum 3 platforms are required to 
safely arrive and depart all trains.

Example 2:


Input: n = 3
arr[] = {0900, 1100, 1235}
dep[] = {1000, 1200, 1240}
Output: 1
Explanation: Only 1 platform is required to 
safely manage the arrival and departure 
of all trains.

# Solution

```python
def minimumPlatform(self,n,arr,dep):
        # code here
        arr = sorted(arr)
        dep = sorted(dep)
        
        platform = 1
        min_platform = platform 
        arr_idx, dep_idx = 1,0
        
        while arr_idx < n and dep_idx < n:
            # equal is imp so as not to miss case when arrival and departure time is same
            # in case of same, we still need more platform.
            if arr[arr_idx] <= dep[dep_idx]:
                platform += 1
                arr_idx += 1
                min_platform = max(min_platform, platform)
            else:
                platform -=1
                dep_idx +=1
                
        return min_platform

```