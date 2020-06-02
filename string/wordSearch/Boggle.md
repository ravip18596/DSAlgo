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

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

```text
Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
``  `

`Solution`

```go
package main
type Trie struct{
    isEnd bool
    Nodes []*Trie
}

func Constructor() Trie{
    t := Trie{}
    t.Nodes = make([]*Trie,27,27)
    for i:=0;i<27;i++{
        t.Nodes[i]=nil
    }
    return t
}

func (this *Trie) Insert(word string){
    for _,c:=range word{
        if this.Nodes[c-96] == nil{
            t := Constructor()
            this.Nodes[c-96] = &t
        }
        this = this.Nodes[c-96]
    }
    this.isEnd = true
}

func (this *Trie) SearchPrefix(prefix string) *Trie{
    for _,c:=range prefix{
        if this.Nodes[c-96] != nil{
            this = this.Nodes[c-96]
        }else{
            return nil
        }
    }
    return this
}

func findWords(board [][]byte, words []string) []string {
    var result []string
    trie := Constructor()
    m := make(map[string]bool)
    for _,word :=range words{
        trie.Insert(word)
    }    
    for i:=0;i<len(board);i++{
        for j:=0;j<len(board[0]);j++{
            var s []byte
            if trie.SearchPrefix(string(board[i][j]))!=nil{
                dfs(board,i,j,s,&trie,&result,m)
            }
        }
    }
    return result
}

func dfs(board [][]byte,i,j int,s []byte,trie *Trie,result *[]string,m map[string]bool){
    if i<0 || i>= len(board) || j<0 || j>= len(board[0]){
        return
    }
    s = append(s,board[i][j])
    mm := trie.SearchPrefix(string(s))
    if mm != nil {
        if mm!= nil && mm.isEnd{
            if _,ok:=m[string(s)];!ok{
                *result = append(*result,string(s))
                m[string(s)]=true
            }
        }
        xd := []int{1,0,-1,0}
        yd := []int{0,1,0,-1}
        temp := board[i][j]
        board[i][j]='`'
        for k:=0;k<4;k++{
            x := i+xd[k]
            y := j+yd[k]
            dfs(board,x,y,s,trie,result,m)
        }
        board[i][j] = temp
        s = s[:len(s)-1]
    }
}
```
