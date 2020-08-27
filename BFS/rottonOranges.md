```text
In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return -1 instead.
```
Example
-------
![](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)
```text
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```
Solution
--------
`BFS solution O(n) - no of grid cells`
```go
package main
type pos struct{
    x,y int
}

func orangesRotting(grid [][]int) int {
    queue := make([]pos,0)
    //enqueue at end and dequeue at front
    freshOranges := 0
    for i:=0;i<len(grid);i++{
        for j:=0;j<len(grid[0]);j++{
            if grid[i][j]==1{
                freshOranges++
            }else if grid[i][j]==2{
                //rotten oranges
                queue = append(queue,pos{x:i,y:j})      
            }
        }
    }
    if freshOranges==0{
        //no fresh oranges left
        return 0
    }
    minutes := 0
    for len(queue)>0 && freshOranges>0{
        minutes++
        size := len(queue)
        for x:=0;x<size;x++{
            frontRottenOrange := queue[0]
            queue = queue[1:] //dequeue
            xarr := []int{-1,0,1,0}
            yarr := []int{0,-1,0,1}
            for k:=0;k<len(xarr);k++{
                i := frontRottenOrange.x + xarr[k]
                j := frontRottenOrange.y + yarr[k]
                if isSafe(i,j,len(grid),len(grid[0])){
                    if grid[i][j]==1{
                        grid[i][j]=2
                        freshOranges--
                        nextpos := pos{x:i,y:j}
                        queue = append(queue,nextpos) //enqueue   
                    }
                }
            }
        }
    }
    if freshOranges==0{
        return minutes
    }
    return -1
}

func isSafe(i,j,x,y int) bool{
    if i<0 || i>=x || j<0 || j>=y{
        return false
    }
    return true
}
```
`BFS solution Level order traversal`
```go
package main
type pos struct{
    x,y int
}

func orangesRotting(grid [][]int) int {
    queue := make([]*pos,0)
    //enqueue at end and dequeue at front
    freshOranges := 0
    for i:=0;i<len(grid);i++{
        for j:=0;j<len(grid[0]);j++{
            if grid[i][j]==1{
                freshOranges++
            }else if grid[i][j]==2{
                //rotten oranges
                queue = append(queue,&pos{x:i,y:j})      
            }
        }
    }
    if freshOranges==0{
        //no fresh oranges left
        return 0
    }
    queue = append(queue,nil)
    //first layer
    minutes := 0
    for len(queue)>0{
        frontRottenOrange := queue[0]
        queue = queue[1:] //dequeue
        if frontRottenOrange==nil{
            if len(queue)>0{
                queue = append(queue,nil)
            }
            minutes++
        }else{
            xarr := []int{-1,0,1,0}
            yarr := []int{0,-1,0,1}
            for k:=0;k<len(xarr);k++{
                i := frontRottenOrange.x + xarr[k]
                j := frontRottenOrange.y + yarr[k]
                if isSafe(i,j,len(grid),len(grid[0])) && grid[i][j]==1{
                    //mark fresh orange rotten
                    grid[i][j]=2
                    //reduce the no of fresh oranges available
                    freshOranges--
                    nextpos := pos{x:i,y:j}
                    queue = append(queue,&nextpos) //enqueue   
                }
            }
        }
        
    }
    if freshOranges==0{
        return minutes-1
    }
    // not possible
    return -1
}

func isSafe(i,j,x,y int) bool{
    if i<0 || i>=x || j<0 || j>=y{
        return false
    }
    return true
}
```