# Searching

### Sorted Array Search

You are given a sorted array arr containing distinct integers. Your task is to implement a function search_position that, given a target value, returns the index where the 
target is found in the array. If the target is not present, return the index where it would be if inserted in order.

```text
Input: arr = [1,3,5,6], target = 5
Output: 2
```

```text
Input: arr = [1,3,5,6], target = 2
Output: 1
```

```cpp
int search_position(vector<int>& arr, int target) {
        int l = 0;
        int r = arr.size();

        while(l < r)
        {
          int mid = (l+r)>>1;
          if(arr[mid] < target)
          {
            l = mid+1;
          }else{
            r = mid;
          }
        }
        return l; 
    }
```

