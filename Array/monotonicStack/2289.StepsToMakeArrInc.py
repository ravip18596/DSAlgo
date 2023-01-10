from typing import List

def totalSteps(nums: List[int]) -> int:
    """
    Intuition
    ---------------
    Increasing array => monotonic decreasing stack
    remove the top number from stack that is no larger than A[i], and record the maximum step number from these popped numbers.
    """
    st = [(nums[0], 0)]
    steps = 0
    for i in range(1, len(nums)):
        time = 0
        while st and st[-1][0] <= nums[i]:
            time = max(time, st[-1][1])
            st.pop(len(st)-1)
        
        if len(st) == 0:
            # an empty stack implies that this is the largest element seen so far
            time = 0
        else:
            time += 1

        steps = max(steps, time)
        st.append((nums[i], time))

    return steps

if __name__ == '__main__':
    steps = totalSteps([5,3,4,4,7,3,6,11,8,5,11])
    print(steps)