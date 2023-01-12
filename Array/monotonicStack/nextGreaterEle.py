from typing import List

def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    n = len(nums2)
    st = [0]
    m = {} 
    for i in range(1,n):
        while st and nums2[st[-1]] < nums2[i]:
            top = st.pop()
            m[nums2[top]] = nums2[i]

        st.append(i)
    
    while st:
        top = st.pop()
        m[nums2[top]] = -1

    #print(m)
    for i in range(len(nums1)):
        nums1[i] = m[nums1[i]]

    return nums1


'''
Problem
NGE

Input: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1

Input: 
N = 5, arr[] [6 8 0 1 3]
Output:
8 -1 1 3 -1
'''

'''
Solution
'''
# maintain a decreasing monotonic stack
def nextLargerElement(self,arr,n):
    #code here
    result = [0]*n
    stack = [0]

    for i in range(1,n):
        while stack and arr[i] > arr[stack[-1]]:
            top = stack.pop()
            result[top] = arr[i]
        
        stack.append(i)
    
    while stack:
        top = stack.pop()
        result[top] = -1
        
    return result