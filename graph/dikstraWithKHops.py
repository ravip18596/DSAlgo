"""
There are `n` cities connected by some number of flights. You are given an array `flights`
where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city
`from_i` to city `to_i` with cost `price_i`.

You are also given three integers `src`, `dst`, and `k`. Return the cheapest price from
`src` to `dst` with at most `k` stops. If there is no such route, return -1.

Constraints:
- 1 <= n <= 100
- 0 <= len(flights) <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= from_i, to_i < n and from_i != to_i
- 1 <= price_i <= 10^4
- There will not be any multiple flights between two cities.
- 0 <= src, dst, k < n and src != dst
"""

from typing import List
from collections import defaultdict
import heapq

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in flights:
        if u == src and v == dst and k == 0:
            return w
        graph[u].append((v, w))

    # (dist, node, stops)
    queue = [(0, src, 0)]
    distance = {}
    for i in range(n):
        distance[i] = float('inf')

    best_stops = [float('inf')]*n

    while queue:
        dist, node, stops = heapq.heappop(queue)
        if node == dst:
            return dist
        if stops > k:
            continue
        if stops >= best_stops[node]:
            continue

        best_stops[node] = stops
        distance[node] = dist

        for neigh_node, neigh_dist in graph[node]:
            heapq.heappush(queue, (dist+neigh_dist, neigh_node, stops+1))

    return -1

if __name__ == '__main__':
    flights =  [[0,1,100], [1,2,100], [2,0,100], [1,3,600], [2,3,200]]
    print(findCheapestPrice(n=4, flights=flights, src=0, dst=3, k=1))

    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    print(findCheapestPrice(n=3, flights=flights, src=0, dst=2, k=0))