from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    # monotonic increasing stack
    n, max_area = len(heights), 0
    st = [0]
    heights += [0]
    for i in range(1,n+1):
        while st and heights[st[-1]] > heights[i]:
            top = st.pop()
            if st:
                width = (i - st[-1] - 1)
            else:
                width = i
            
            # since monotonically inc stack, top will be of largest height in the left.
            area = heights[top] * width
            max_area = max(max_area, area)
        
        st.append(i)
    
    return max_area


if __name__ == '__main__':
    print(largestRectangleArea([2,1,5,6,2,3]))
    print(largestRectangleArea([2,1,2]))
    print(largestRectangleArea([2,4]))
    print(largestRectangleArea([1,1]))
    print(largestRectangleArea([1]))