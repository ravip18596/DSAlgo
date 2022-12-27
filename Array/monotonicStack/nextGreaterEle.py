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