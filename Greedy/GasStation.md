```text
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```
Solution
--------

### Golang
```go
package main
func canCompleteCircuit(gas []int, cost []int) int {
    var totalCost,startIndex,startcost int
    for i:=0;i<len(gas);i++{
        totalCost += (gas[i]-cost[i])
        startcost += (gas[i]-cost[i])
        if startcost<0{
            startIndex=i+1
            //starting again resets the cost
            startcost=0
        }
    }
    // if total cost is less than zero then it 
    // cannot complete cycle
    if totalCost<0{
        return -1
    }
    return startIndex
}
```

### Python

```python
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    start_index, start_cost, total_cost = 0, 0, 0
    n = len(cost)
    for i in range(n):
        journey_cost = gas[i] - cost[i]
        total_cost += journey_cost
        start_cost += journey_cost
        if start_cost < 0:
            start_index, start_cost = i+1, 0
        
    # if total gas is less total gas required then circular journey not possible
    return -1 if total_cost < 0 else start_index
```
