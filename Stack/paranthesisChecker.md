# Problem

# Solution

```python
def paranthesis_checker(x: str):
    # code here
    stack = []
    balanced = True
    for c in x:
        if c=='{':
            stack.append('}')
        elif c=='[':
            stack.append(']')
        elif c=='(':
            stack.append(')')
        elif c in '}])':
            # if closing brackets and then stack is empty
            if len(stack)==0:
                balanced = False
                break
            
            top = stack.pop()
            if top!=c:
                balanced = False
                break
        
    # if stack is not empty then not balanced
    if len(stack) > 0:
        balanced = False
    
    return balanced
```

### Solution 2

```python
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        m = {'(':')', '{': '}', '[':']'}
        for c in s:
            if c in ['(', '{', '[']:
                st.append(m[c])
            elif c in [')', '}', ']']:
                if len(st)==0 or st[-1] != c:
                    return False
                
                st.pop()

        return len(st) == 0
```