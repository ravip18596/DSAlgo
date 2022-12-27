"""
Input: 
N = 7, price[] = [100 80 60 70 60 75 85]
Output:
1 1 1 2 1 4 6
Explanation:
Traversing the given input span for 100 
will be 1, 80 is smaller than 100 so the 
span is 1, 60 is smaller than 80 so the 
span is 1, 70 is greater than 60 so the 
span is 2 and so on. Hence the output will 
be 1 1 1 2 1 4 6.
"""

def calculateSpan(a,n):
    #code here
    # monotonically decreasing stack
    span = [1]*n
    st = [0]
    i = 1
    
    while i<n:
        while st and a[st[-1]] <= a[i]:
            st.pop()
            
        if st:
            span[i] = i-st[-1]
        else:
            span[i] = i+1
            
        st.append(i)
        i+=1
            
    return span