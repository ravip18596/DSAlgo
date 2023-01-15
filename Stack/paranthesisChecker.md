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