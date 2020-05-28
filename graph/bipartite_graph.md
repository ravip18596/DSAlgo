#Bipartite graph problems

### Question 1

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

```
Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
```

```go
func possibleBipartition(N int, dislikes [][]int) bool {
    //bfs solution
    visited := make([]bool,N+1) //whether node visited or not for traversal
    adj := make([][]int,N+1) //adjacency matrix of graph
    color := make([]int,N+1) //default color is 0 for all nodes. 1 is red and 2 is blue
    
    for _,d:=range dislikes{
        u:=d[0]
        v:=d[1]
        adj[u] = append(adj[u],v)
        adj[v] = append(adj[v],u)
    }
    var queue []int
    for i:=1;i<=N;i++{
        if !visited[i]{
            queue = enqueue(queue,i)
            color[i] = 1 // red color
        }
        for len(queue)>0{
            var u int
            queue,u = dequeue(queue)
            if visited[u]{
                continue
            }
            visited[u] = true
            for _,neigh:=range adj[u]{
                if color[neigh]==color[u]{
                    return false //becoz in bigraph, adjacent or neigh edge is between disliked set only and disliked set are represented by diff colors. if colors are same then nodes are in same set hence not bigraph
                }
                //assign alter color to neigh
                if color[u]==1{
                    color[neigh]=2
                }else if color[u]==2{
                    color[neigh]=1 
                }
                queue = enqueue(queue,neigh)
            }
        }
    }
    
    return true
}

func enqueue(queue[] int, element int) []int {
  queue = append(queue, element); // Simply append to enqueue.
  return queue
}

func dequeue(queue[] int) ([]int,int) {
  element := queue[0]; // The first element is the one to be dequeued.
  return queue[1:],element; // Slice off the element once it is dequeued.
}

```