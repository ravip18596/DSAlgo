## Problem

Given a grid of size n*n filled with 0, 1, 2, 3. Check whether there is a path possible from the source to destination. You can traverse up, down, right and left.
The description of cells is as follows:

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Wall.
Note: There are only a single source and a single destination.

## Example

Input: grid = {{1,3},{3,2}}
Output: 1
Explanation: The grid is-
1 3
3 2
There is a path from (0,0) i,e source to (1,1) 
i,e destination.

## Solution

- Time: O(N^2)
- Space: O(1) extra space, O(N^2) stack space

```python
def is_Possible(self, grid):
		#Code here
		
		directions = [(-1,0), (0,1), (1,0), (0, -1)]
		def dfs(i,j):
		    if i<0 or j<0 or i>=r or j>=c or grid[i][j]==0:
		        return False
		        
		    result = grid[i][j]==2
		    
		    grid[i][j] = 0
		    for d in directions:
		        x, y = i+d[0], j+d[1]
		        result = result or dfs(x,y)
		    
		    return result
		        
		r,c = len(grid), len(grid[0])
		for i in range(r):
		    for j in range(c):
		        if grid[i][j] == 1:
		            return dfs(i,j)
		
		return False
```

- C++

```cpp
#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    //Function to find whether a path exists from the source to destination.
    int directions[4][2] = {{-1,0}, {0,1}, {1,0}, {0,-1}};
    
    bool dfs(vector<vector<int>> &grid, int i, int j)
    {
        int rows = grid.size();
        int cols = grid[0].size();
        
        if(i<0 || j<0 || i>=rows || j>=cols || grid[i][j] == 0)
        {
            return false;
        }
        
        bool result = false;
        if(grid[i][j] == 2){
            result = true;
        }
        grid[i][j] = 0;
        int x,y;
        for(int k=0;k<4;k++)
        {
            x = i+directions[k][0];
            y = j+directions[k][1];
            result = result || dfs(grid,x,y);
        }
        return result;
    }
    
    bool is_Possible(vector<vector<int>>& grid) 
    {
        //code her
        int rows = grid.size();
        int cols = grid[0].size();
        
        for(int i=0;i<rows;i++)
        {
            for(int j=0;j<cols;j++)
            {
                if(grid[i][j] == 1){
                    return dfs(grid, i,j);
                }
            }
        }
        return false;
    }
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		vector<vector<int>>grid(n, vector<int>(n, -1));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				cin >> grid[i][j];
			}
		}
		Solution obj;
		bool ans = obj.is_Possible(grid);
		cout << ((ans) ? "1\n" : "0\n");
	}
	return 0;
}
```