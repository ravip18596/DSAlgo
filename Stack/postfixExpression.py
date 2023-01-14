'''
Problem: Evaluate Postfix expression

Input: S = "231*+9-"
Output: -4

Input: S = "123+*8-"
Output: -3
'''

def evaluatePostfix(self, S):
    #code here
    stack = []
    for c in S:
        if c.isnumeric():
            stack.append(int(c))
        elif c == '*':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1*n2)
        elif c == '/':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1//n2)
        elif c == '+':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1+n2)
        elif c == '-':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1-n2)
            
    return stack[-1]