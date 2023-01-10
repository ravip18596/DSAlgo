## Problem
Given a directed acyclic graph(DAG) with n nodes labeled from 0 to n-1. Given edges, s and d ,count the number of ways to reach from s to d.There is a directed Edge from vertex edges[i][0] to the vertex edges[i][1].

Input: edges = {{0,1},{0,3},{1,2},{3,2}}, 
n = 4, s = 0, d = 2
Output: 2

## Solution

Time: O(2^n)
Space: O(n+e)

```python
def possible_paths(self, edges, n, s, d):
    #Code here
    def dfs(adj, i, d):
        cnt = 0
        if i==d:
            cnt+=1
        
        for j in adj[i]:
            cnt += dfs(adj, j, d)
                
        return cnt
        
    adj = [[] for i in range(n)]
    
    for edge in edges:
        adj[edge[0]].append(edge[1])
    
    total_cnt = dfs(adj,s,d)
    
    return total_cnt
```

```cpp
void dfs(vector<vector<int>> adj, int i, int dest, int& cnt)
    {
        if(i==dest){
            cnt++;
        }
        
        for(auto neigh: adj[i]){
            // DAG so no cycle
            dfs(adj, neigh, dest, cnt);
        }
    }
	int possible_paths(vector<vector<int>>edges, int n, int s, int d){
	    // Code here
	    vector<vector<int>> adj(n);
	    
	    for(auto edge: edges){
	        int u = edge[0];
	        int v = edge[1];
	        adj[u].push_back(v);
	    }
	    
	    int cnt = 0;
	    dfs(adj, s, d, cnt);
	    
	    return cnt;
	}
```