Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
 
```text
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```

`Solution`
```go
/**
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

After sorting by height - 
[[7 0] [7 1] [6 1] [5 0] [5 2] [4 4]] 

before copy - [[]]
after copy -  [[]]
after insert -  [[7 0]]

before copy - [[7 0] []]
after copy -  [[7 0] []]
after insert -  [[7 0] [7 1]]

before copy - [[7 0] [7 1] []]
after copy -  [[7 0] [7 1] [7 1]]
after insert -  [[7 0] [6 1] [7 1]]

before copy - [[7 0] [6 1] [7 1] []]
after copy -  [[7 0] [7 0] [6 1] [7 1]]
after insert -  [[5 0] [7 0] [6 1] [7 1]]

before copy - [[5 0] [7 0] [6 1] [7 1] []]
after copy -  [[5 0] [7 0] [6 1] [6 1] [7 1]]
after insert -  [[5 0] [7 0] [5 2] [6 1] [7 1]]

before copy - [[5 0] [7 0] [5 2] [6 1] [7 1] []]
after copy -  [[5 0] [7 0] [5 2] [6 1] [7 1] [7 1]]
after insert -  [[5 0] [7 0] [5 2] [6 1] [4 4] [7 1]]
**/
package main
import "sort"
func reconstructQueue(people [][]int) [][]int {
    sort.Slice(people,func(i,j int)bool{
        if people[i][0] == people[j][0]{
            return people[i][1]<people[j][1]
        }
        return people[i][0] > people[j][0]
    })
    //fmt.Println(people,len(people))
    var queue [][]int
    for i:=0;i<len(people);i++{
        index := people[i][1]
        value := people[i]
        //insert dummy
        queue = append(queue,[]int{}) // this step increases the size by 1 for next step
        //copy queue [index..n+1] to [index+1..n+1]
        //fmt.Println("before copy -",queue)
        copy(queue[index+1:],queue[index:]) 
        //fmt.Println("after copy - ",queue)
        queue[index] = value
        //fmt.Println("after insert - ",queue)
        //fmt.Println("")
    }
    return queue
}
```