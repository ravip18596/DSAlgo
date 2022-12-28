## Problem

Given a dictionary of distinct words and an M x N board where every cell has one character. Find all possible words from the dictionary that can be formed by a sequence of adjacent characters on the board. We can move to any of 8 adjacent characters

## Examples

Input:
N = 4
dictionary = {"GEEKS","FOR","QUIZ","GO"}
R = 3, C = 3 
board = {{G,I,Z},{U,E,K},{Q,S,E}}
Output:
GEEKS QUIZ
Explanation: 
G I Z
U E K
Q S E 
Words we got is denoted using same color.

## Solution

```python
def wordBoggle(self,board,dictionary):
    # return list of words(str) found in the board
    directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    def dfs(i, j, word, idx):
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != word[idx]:
            return False
            
        result = idx==len(word)-1
        temp = board[i][j]
        board[i][j] = '*'
        for d in directions:
            x,y = i+d[0], j+d[1]
            result = result or dfs(x,y, word,idx+1)
            
        board[i][j] = temp
        return result
    
    
    found = {}
    r, c = len(board), len(board[0])
    for word in dictionary:
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    status = dfs(i,j,word,0)
                    if status and word not in found.keys():
                        found[word] = 1
            
    return [key for key in found.keys()]
```