Solution
--------
`Complexity`

DFS time complexity is O(|E| + |V|), attempting to visit each edge at most twice. (the second attempt will immediately return.)
As the graph is always a connected graph, |E| >= |V|.

`time complexity` = O(|E|).
`Space complexity` = O(graph) + O(rank) + O(connections) = 3 * O(|E| + |V|) = O(|E|).

`Python`
```python
import collections
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        result = []
        def dfs(depth,curr,prev):
            min_depth[curr] = depth
            for neigh in graph[curr]:
                if neigh == prev:
                    continue
                if min_depth[neigh] == 0: # not visited
                    # then dfs
                    dfs(depth+1,neigh,curr)
                    
                min_depth[curr] = min(min_depth[curr], min_depth[neigh])
                if min_depth[neigh] >= depth+1:# if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection
                    result.append([curr, neigh])
                    
            
        graph = collections.defaultdict(list)
        min_depth = [0]*n
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        dfs(1,0,-1)
        return result
```