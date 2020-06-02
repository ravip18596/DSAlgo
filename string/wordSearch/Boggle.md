Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

```Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```

`Solution`

```go
package main
func exist(board [][]byte, word string) bool {
    for i:=0;i<len(board);i++{
        for j:=0;j<len(board[0]);j++{
            if board[i][j]==byte(word[0]) && dfs(board,i,j,word,0){
                return true
            }
        }
    }
    return false
}

func dfs(board [][]byte,i,j int,word string,index int) bool{
    if i<0 || i>= len(board) || j<0 || j>= len(board[0]){
        return false
    }
    if byte(word[index])==board[i][j]{
        if index==len(word)-1{
            return true
        }
        xd := []int{1,0,-1,0}
        yd := []int{0,1,0,-1}
        var result bool
        temp := board[i][j]
        board[i][j]='*'
        for k:=0;k<4;k++{
            x := i+xd[k]
            y := j+yd[k]
            result = result || dfs(board,x,y,word,index+1)
        }
        board[i][j] = temp
        return result
    }else{
        return false
    }
}
```