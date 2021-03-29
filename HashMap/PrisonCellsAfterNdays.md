Problem
-------
There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

- If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied. 
- Otherwise, it becomes vacant.

Return the state of the prison after n days (i.e., n such changes described above).

Examples
--------
```text
Input: cells = [0,1,0,1,1,0,0,1], n = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```

Solution
--------
`Intution`

Note that cells.length = 8, and cells[0] and cells[7] will become 0.
In fact, cells have only 2 ^ 6 = 64 different states.
And there will be a loop.

- Time - O(64)
- Space - O(64)

1) utility method next_cell finds the next day's cell states
2) Iterate and store the cell states that occurred previously
3) If there's no cycle, return. If there's a cycle, break the loop and rerun N%cycle times to find the target cell states

`Python`
```python
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        state_map = set()
        cnt,has_cycle = 0,False
        for i in range(n):
            next_cell = self.next_day_cell(cells)
            next_state =  ''.join(str(j) for j in next_cell)
            if next_state not in state_map:
                state_map.add(next_state)
                cnt+=1
            else:
                has_cycle = True
                break
                
            cells = next_cell
    
        if has_cycle:
            n = n%cnt
            for i in range(n):
                cells = self.next_day_cell(cells)
                
        return cells
            
        
    def next_day_cell(self,cells:List[int])->List[int]:
        temp = [0]*len(cells)
        for i in range(1,len(cells)-1):
            temp[i] = 1 if cells[i-1]==cells[i+1] else 0
        return temp    
        
```
