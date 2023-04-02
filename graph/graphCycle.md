Question 1
----------
`Detect cycle in an undirected graph`



```
bool util(vector<int> g[],int i,vector<int>& vis)
{
    if(vis[i]==2){
        return true;
    }
    if(vis[i]==1){
        return false;
    }
    vis[i]=1;
    for(int j=0;j<g[i].size();j++){
        if(util(g,g[i][j],vis)==true){
            return true;
        }
    }
    vis[i]=2;
    return false;
}

bool isCyclic(vector<int> g[], int V)
{
   // Your code here
   vector<int> vis = vector<int>(V,0);
   for(int i=0;i<V;i++){
       if(vis[i]==0){
           if(util(g,i,vis)==true){
               return true;
           }
       }
   }
   return false;
}
```

###Question 2

`Detect cycle in a directed graph`

```
bool util(vector<int> adj[],int i,vector<bool>& vis,vector<bool>& rec)
{
    if(vis[i]==false){
        vis[i]=true;
        rec[i]=true;
    }
    for(int j=0;j<adj[i].size();j++){
        int v = adj[i][j];
        if(!vis[v] && util(adj,v,vis,rec)){
            return true;
        }else if(rec[v]){
            return true;
        }
    }
    rec[i]=false;
    return false;
}

bool isCyclic(int V, vector<int> adj[])
{
    // Your code here
    vector<bool> vis = vector<bool>(V,false);
    vector<bool> rec = vector<bool>(V,false);
   for(int i=0;i<V;i++){
       if(!vis[i]){
           if(util(adj,i,vis,rec)==true){
               return true;
           }
       }
   }
   return false;
}
```

`Given the total number of tasks N and a list of prerequisite pairs P, find if it is possible to finish all tasks.`

Input: 
N = 4, P = 3
prerequisites = {{1,0},{2,1},{3,2}}
Output:
Yes

Input:
N = 2, P = 2
prerequisites = {{1,0},{0,1}}
Output:
No

`Solution`

- Construct graph 
- If there is cycle then not possible else possible

`Python`

```python
class Solution:
    def dfs(self, node, visited, on_path, adj):
        if visited[node]:
            # Node is already visited but there is no cycle.
            return False
            
        # mark unvisited node visited
        visited[node] = True
        on_path[node] = True
        # Traverse its neighbours
        for j in adj[node]:
            # Either neigh already met in path or found cycle from dfs on neigh
            # then propagate true
            if on_path[j] or self.dfs(j, visited, on_path, adj):
                return True
        
        on_path[node] = False   
        return False
        
    def isPossible(self,N,prerequisites):
        #code here
        adj = [[] for _ in range(N)]
        
        for u,v in prerequisites:
            adj[v].append(u)
        
        visited = [False]*N
        on_path = [False]*N # record the visited nodes in the current DFS 
        for i in range(N):
            if not visited[i]:
                if self.dfs(i, visited, on_path, adj):
                    # cycle is there so not possible
                    return False
        
        return True
```