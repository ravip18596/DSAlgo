# Stack

## Monotonic Stack

### NGE (Next Greater Element)

[https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1](https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1)

maintain a monotonic decreasing stack

```python
def nextLargerElement(arr):
    # code here
    # monotonic decreasing stack
    stack = []
    nge = [-1]*len(arr)
    for i in range(len(arr)):
        while len(stack) > 0 and arr[stack[-1]] < arr[i]:
            j = stack.pop()
            nge[j] = arr[i]
        
        stack.append(i)
        
    return nge
```

### PGE (Previous Greater Element)

maintain a monotonic decreasing stack

```python
def prevGreaterElement(arr):
    n = len(arr)
    pge = [0]*n
    stack = []
    for i in range(n):
        while len(stack) > 0 and stack[-1] < arr[i]:
            stack.pop()

        if len(stack) == 0:
            pge[i] = -1
        else:
            pge[i] = stack[-1]

        stack.append(arr[i])
    
    return pge

arr = [ 10, 4, 2, 20, 40, 12, 30 ]
print(prevGreater(arr))
# Output [-1, 10, 4, -1, -1, 40, 40]
```

### NSE (Next smaller element)

maintain a monotonic increasing stack

```python
def nextSmallerElement(arr):
    n = len(arr)
    stack = []
    nse = [-1]*n
    for i in range(n):
        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            j = stack.pop()
            nse[j] = arr[i]

        stack.append(i)

    return nse

arr = [4, 8, 5, 2, 25]
print(nextSmallerElement(arr))
# Output: [2, 5, 2, -1, -1]
```

### PSE (Previous Smaller Element)

maintain a monotonic increasing stack

```python
def prevSmallerElement(arr):
    n = len(arr)
    pse = [0]*n
    stack = []
    for i in range(n):
        while len(stack) > 0 and stack[-1] > arr[i]:
            stack.pop()

        if len(stack) == 0:
            pse[i] = -1
        else:
            pse[i] = stack[-1]

        stack.append(arr[i])

    return pse

arr = [2, 3, 4, 5, 1]
print(prevSmallerElement(arr))
# Output [-1 2 3 4 -1]
```

## Largest Rectangle in Histogram

[https://leetcode.com/problems/largest-rectangle-in-histogram/description/](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

- For every bar, I'll find the max area rectangle whose height is that given bar
- area = height X base
- For every i, I am finding the index of the next smaller element
- For every i, I am finding the index of the prev smaller element

$$ Time-Complexity: O(N) $$
$$ Space-Complexity: O(N) $$

```python
def largestRectangleArea(heights: List[int]) -> int:
    n = len(heights)
    area = []
    nse = [n]*n
    pse = [-1]*n

    stack = []
    # maintain a monotonic increasing stack
    for i in range(n):
        while len(stack) > 0 and heights[stack[-1]] > heights[i]:
            j = stack.pop()
            nse[j] = i

        stack.append(i)
    
    stack = []
    for i in range(n):
        while len(stack) > 0 and heights[stack[-1]] > heights[i]:
            stack.pop()

        if len(stack) == 0:
            pse[i] = -1
        else:
            pse[i] = stack[-1]
        
        stack.append(i)

    for i in range(n):
        area[i] = heights[i] * (nse[i] - pse[i] - 1)

    return max(area)

heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))
# Output: 10
```

## Maximal Rectangle

[https://leetcode.com/problems/maximal-rectangle/description/](https://leetcode.com/problems/maximal-rectangle/description/)

- Every rectangle is standing on some row as base
- For every row as base, I find the max area rectangle containing only 1's
- For (i = 0 to m):
    - find the height array
    - find the max area rectangle using above problem (largest area in an histogram)
    - ans = max(ans, max_area)

$$ Time-Complexity: O(M*N) $$
$$ Space-Complexity: O(N) $$

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = [0]*n
        nse = [n]*n
        pse = [-1]*n

        stack = []
        # maintain a monotonic increasing stack
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                nse[j] = i

            stack.append(i)
        
        stack = []
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                stack.pop()

            if len(stack) == 0:
                pse[i] = -1
            else:
                pse[i] = stack[-1]
            
            stack.append(i)

        for i in range(n):
            area[i] = heights[i] * (nse[i] - pse[i] - 1)

        return max(area)


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        height = [0] * n
        for j in range(n):
            height[j] = int(matrix[0][j])

        for i in range(m):
            area = self.largestRectangleArea(height)
            max_area = max(max_area, area)
            if i<m-1:
                for j in range(n):
                    if matrix[i+1][j] == "1":
                        height[j] = height[j] + 1
                    else:
                        height[j] = 0

        return max_area    
```


## Sliding Window Maximum

[https://leetcode.com/problems/sliding-window-maximum/description/](https://leetcode.com/problems/sliding-window-maximum/description/)

```python
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    stack = []
    for i in range(k):
        # maintain a monotonically decreasing stack
        while len(stack)>0 and stack[-1] < nums[i]:
            stack.pop()

        stack.append(nums[i])
    
    ans = []
    i = 0
    while i+k<len(nums):
        ans.append(stack[0])
        #nums[i] be removed and nums[i+k] will be added
        pop_ele = nums[i]
        push_ele = nums[i+k]
        if pop_ele == stack[0]:
            # pop front
            stack = stack[1:]
        
        while len(stack) > 0 and stack[-1] < push_ele:
            stack.pop()

        stack.append(push_ele)
        i+=1
    
    ans.append(stack[0])
    return ans
```

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        for(int i=0; i<k; i++) {                                          // Maintain a monotonically decreasing queue, the front element will have the maximum element in that window.
            while(!dq.empty() && dq.back()<nums[i]) {
                dq.pop_back();
            }
            dq.push_back(nums[i]);                   // Trying to create a deque for the first subarray of size k. 
        }

        // Slide the window
        vector<int> ans;
        for(int i=0; i+k<nums.size() ; i++) {
            ans.push_back(dq.front());                                   // Front element is the maximum in the previous window.

            int pop_element = nums[i];                            // In the next window, ith element will be thrown out of the window and i+kth element will be added in the deque.
            int push_element = nums[i+k];    

            // Here we throw the element out of the deque that can never be the maximum of any sliding window, hence we maintain a monotonically decreasing deque.
          
            if(dq.front() == pop_element) {
                dq.pop_front();
            }

            while(!dq.empty() && dq.back()<push_element) {
                dq.pop_back();
            }    
            dq.push_back(push_element);
        }

        ans.push_back(dq.front());
        return ans;
    }
};
```

## Reverse Polish Notation

[https://leetcode.com/problems/evaluate-reverse-polish-notation/description/](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

```python
def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            p2 = stack.pop()
            p1 = stack.pop()
            print(f'{p1}{token}{p2}')
            ans = 0
            if token == '+':
                ans = p1+p2
            elif token == '-':
                ans = p1-p2
            elif token == '*':
                ans = p1*p2
            elif token == '/':
                ans = p1/p2
                if ans < 0 and ans >= -1:
                    ans = 0
                else:
                    ans = int(ans)

            stack.append(ans)
        else:
            stack.append(int(token))

    return stack[-1]
```

