# Problem
Given a weighted, undirected and connected graph of V vertices and an adjacency list adj
adj[i] = (edge_node, weight)
Return a list of integers denoting shortest distance between each node and Source vertex S.


```python
import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        inf = int(1e9)+7
        
        pq = []
        dist = [inf]*V
        
        dist[S] = 0
        heapq.heappush(pq, (0, S))
        
        while len(pq)>0:
            _, i = heapq.heappop(pq)
            
            for neigh, weight in adj[i]:
                if dist[neigh] > dist[i] + weight:
                   dist[neigh] = dist[i] + weight
                   heapq.heappush(pq, (dist[neigh], neigh))
                   
        return dist
```