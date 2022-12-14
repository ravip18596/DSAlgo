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

- Python BFS 1
using None as level counter

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # count how many fresh oranges are there
        rows, cols = len(grid), len(grid[0])
        queue = []
        
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        queue.append(None)
        if fresh == 0:
            return 0        

        directions = [(-1,0), (0, 1), (1, 0), (0, -1)]
        level = 0
        # first level
        while len(queue) > 0:
            front = queue[0]
            # deque
            queue = queue[1:]
            if front is None:
                level += 1
                if len(queue)>0:
                    queue.append(None)
            else:
                i, j = front
                for k in range(len(directions)):
                    new_i, new_j = i + directions[k][0], j + directions[k][1]

                    if new_i<rows and new_i>=0 and new_j<cols and new_j>=0 and grid[new_i][new_j] == 1:
                        queue.append((new_i, new_j))
                        # mark fresh orange visited by making it rotten
                        grid[new_i][new_j] = 2
                        fresh -= 1
                    
        if fresh > 0:
            return -1
    
        return level-1
```

- BFS by passing level info into the queue

Faster
```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # count how many fresh oranges are there
        rows, cols = len(grid), len(grid[0])
        queue = []
        
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        if fresh == 0:
            return 0        

        directions = [(-1,0), (0, 1), (1, 0), (0, -1)]
        level = 0
        # first level
        while len(queue) > 0:
            front = queue[0]
            # deque
            queue = queue[1:]
            i, j, level = front
            for k in range(len(directions)):
                new_i, new_j = i + directions[k][0], j + directions[k][1]

                if new_i<rows and new_i>=0 and new_j<cols and new_j>=0 and grid[new_i][new_j] == 1:
                    queue.append((new_i, new_j, level+1))
                    # mark fresh orange visited by making it rotten
                    grid[new_i][new_j] = 2
                    fresh -= 1
                    
        if fresh > 0:
            return -1
    
        return level
```
