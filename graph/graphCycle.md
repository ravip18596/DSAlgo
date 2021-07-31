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