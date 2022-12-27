from typing import List

def nextGreaterElements(nums: List[int]) -> List[int]:
    # monotonic decreasing stack
    n = len(nums)
    st = [0] # insert start ele index
    nge = [-1]*n
    for i in range(1, 2*n):
        while st and nums[st[-1]%n] < nums[i%n]:
            top = st.pop()
            nge[top%n] = nums[i%n]

        st.append(i)

    return nge

if __name__ == '__main__':
    print(nextGreaterElements([1,2,1]))