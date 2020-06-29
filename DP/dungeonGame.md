`Question`

```text
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

```

![](https://assets.leetcode.com/static_assets/discuss/uploads/files/1470070031420-dungeon.png)

`Solution`
`Go`

```go
package main
func calculateMinimumHP(dungeon [][]int) int {
    rows:=len(dungeon)
    cols := len(dungeon[0])
    hp := make([][]int,rows)
    for i:=0;i<rows;i++{
        hp[i] = make([]int,cols)
    }
    //base cases
    //bottom-right
    hp[rows-1][cols-1]=max(1,1-dungeon[rows-1][cols-1])
    //last row - can only reach from right
    for i:=cols-2;i>=0;i--{
        hp[rows-1][i] = max(1,hp[rows-1][i+1]-dungeon[rows-1][i])
    }
    //last col - can only reach from down
    for i:=rows-2;i>=0;i--{
        hp[i][cols-1] = max(1,hp[i+1][cols-1]-dungeon[i][cols-1])
    }
    for i:=rows-2;i>=0;i--{
        for j:=cols-2;j>=0;j--{
            right := max(1,hp[i+1][j]-dungeon[i][j])
            down :=  max(1,hp[i][j+1]-dungeon[i][j])
            hp[i][j] = min(right,down)
        }
    }
    return hp[0][0]
}

func min(a,b int) int{
    if a<b{
        return a
    }
    return b
}

func max(a,b int) int{
    if a>b{
        return a
    }
    return b
}
```

`Explanation`
```text
With a health array to store each grid's health, we should get the result at [0][0].

Now the question become to how to create a health array using dungeon.

dungeon

-2,-3,3
-5,-10,1
10,30,-5

From the Dungeon grid, we can simply compute health for the [last row][last column].

Now we get

?,?,?
?,?,?
?,?,6

Now because the knight can only move rightward or downward in each step, we can compute all the health value for last row from right to left using its rightward neighbor. we can also compute all the health value for last column from bottom to up using its downward neighbor.

?,?,2
?,?,5
1,1,6

Now, we can compute all the health value using its downward neighbor and rightward neighbor(we use the min value of these 2 health value).

7,5,2
6,11,5
1,1,6

Now we get the answer [0][0], which is 7.
```
    