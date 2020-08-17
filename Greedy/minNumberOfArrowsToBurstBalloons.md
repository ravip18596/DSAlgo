```text
There are a number of spherical balloons spread in two-dimensional
space. For each balloon, provided input is the start and end coordinates
of the horizontal diameter. Since it's horizontal, y-coordinates don't 
matter and hence the x-coordinates of start and end of the diameter suffice.
Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the
x-axis. A balloon with xstart and xend bursts by an arrow shot at x 
if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot.
An arrow once shot keeps travelling up infinitely. The problem is to find 
the minimum number of arrows that must be shot to burst all balloons.
```

`Logic`

```text
we can sort the array of balloons by their ending position.
We can shoot as many following balloons as possible by chosing balloon[i].end 

Time - O(NLogN) Space - O(1)

balloons = [[7,10], [1,5], [3,6], [2,4], [1,4]]

After sorting, it becomes:

balloons = [[2,4], [1,4], [1,5], [3,6], [7,10]]

So first of all, we shoot at position 4, we go through the array and see that all first 4 balloons can be taken care of by this single shot. Then we need another shot for one last balloon. So the result should be 2.
```

```go
package main
//similar to max/min no of meeting rooms required problem
func findMinArrowShots(points [][]int) int {
    if len(points)<=1{
        return len(points)
    }
    //sort by end time
    sort.Slice(points,func(i,j int)bool{
        return points[i][1] < points[j][1]
    })
    var arrows int
    arrows = 1 //becoz assuming first point's end as first ballon 
    lastEndTime := points[0][1]
    for i:=1;i<len(points);i++{
        if lastEndTime >= points[i][0] {
            //it means that this ballon falls in range
            continue
        }
        //out of range, so new arrows
        arrows++
        lastEndTime = points[i][1]
    }
    return arrows
}
```