###Graph Ordering or Topological Sort Questions

###Question 1

`Given a Directed Graph. Find any Topological Sorting of that Graph.`

```cgo
void dfs(int node,vector<int> adj[],vector<bool>& v,stack<int>& s)
{
    v[node]=true;
    for(int j=0;j<adj[node].size();j++){
        int neigh = adj[node][j];
        if(!v[neigh]){
            dfs(neigh,adj,v,s);
        } 
    }
    s.push(node);
}

int* topoSort(int V, vector<int> adj[]) {
    // Your code here
    stack<int> s;
    vector<bool> v = vector<bool>(V,false);
    for(int i=0;i<V;i++){
        if(!v[i]){
            dfs(i,adj,v,s);
        }
    }
    int *result = new int[V];
    int i=0;
    while(!s.empty())
    {
        result[i++] = s.top();
        s.pop();
    }
    return result;
}
```

###Question2

There are a total of n courses you have to take, labeled from 0 to n-1.Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
 
 Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
 
 There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
 
```Example 1:
 
 Input: 2, [[1,0]] 
 Output: [0,1]
 Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
              course 0. So the correct course order is [0,1] .
```              
 
```Example 2:
 
 Input: 4, [[1,0],[2,0],[3,1],[3,2]]
 Output: [0,1,2,3] or [0,2,1,3]
 Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
 ```
 
###Solution 2

```go
package main
func findOrder(numCourses int, prerequisites [][]int) []int {
    // step -1 check if the graph is acyclic directed graph
    var adj [][]int
    adj = make([][]int,numCourses)
    for i:=0;i<len(prerequisites);i++{
        u:=prerequisites[i][1]
        v:=prerequisites[i][0]
        adj[u] = append(adj[u],v)
    }
    //DAG cycle detection code
    var isCyclic bool
    vis := make([]bool,numCourses)
    rec := make([]bool,numCourses)
    for i:=0;i<numCourses;i++{
        if !vis[i] && isCyclicDfs(i,adj,vis,rec){
            isCyclic=true
            break
        }
    }
    if isCyclic{
        return []int{}
    }
    //topological sorting code
    stack := make([]int,0)
    visited := make([]bool,numCourses)
    for i:=0;i<numCourses;i++{
        if !visited[i]{
            topologicalSortUtil(i,adj,visited,&stack)
        }
    }
    reverse(stack)
    return stack
}


func isCyclicDfs(node int,adj [][]int,visited,rec []bool) bool{
    if !visited[node]{
        visited[node]=true
        rec[node]=true
    }
    for _,i:=range adj[node]{
        if !visited[i] && isCyclicDfs(i,adj,visited,rec){
            return true
        }else if rec[i]{
            return true
        }
    }
    rec[node]=false
    return false
}

func topologicalSortUtil(node int,adj [][]int,visited []bool,stack *[]int){
    visited[node] = true
    for _,i:=range adj[node]{
        if !visited[i]{
            topologicalSortUtil(i,adj,visited,stack)
        }
    }
    *stack = append(*stack,node)
}

func reverse(num []int){
    i,j:=0,len(num)-1
    for ;i<j;i,j=i+1,j-1{
        num[i],num[j]=num[j],num[i]
    }
}
```
