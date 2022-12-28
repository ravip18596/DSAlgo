import java.util.*;
import java.lang.*; 

class Test {
    public static void main(String[] args) {
        Solution obj = new Solution();
        int[][] grid = { { 1, 1, 0, 1, 1 },
                    { 1, 0, 0, 0, 0 },
                    { 0, 0, 0, 0, 1 },
                    { 1, 1, 0, 1, 1 }
                   };
 
        // Function Call
        System.out.println("Number of distinct islands is " + obj.countDistinctIslands(grid));
        
    }
}
class Solution {
    // Function to find the number of islands.
    static int[][] dirs = {{-1,0},{0,1}, {1,0}, {0,-1}};

    private static void dfs(int[][] grid, int i, int j, int si, int sj, ArrayList<String> coords) {
        if(i<0 || j<0 || i>=grid.length || j>=grid[0].length || grid[i][j] <= 0) {
            return;
        }
        grid[i][j] = -1;
        coords.add(Integer.toString(i-si) + " " + Integer.toString(j-sj));
        for(int k=0;k<4;k++)
        {
            dfs(grid, i+dirs[k][0], j+dirs[k][1], si, sj, coords);
        }
    }
    public int countDistinctIslands(int[][] grid) {
        // Code here
        HashSet<ArrayList<String>> islands = new HashSet<>();
        ArrayList<String> v;
        for(int i=0;i<grid.length;i++)
        {
            for(int j=0;j<grid[0].length;j++) {
                if(grid[i][j] == 1){
                    v = new ArrayList<>();
                    dfs(grid, i, j, i, j, v);
                    System.out.println(v);
                    islands.add(v);
                }
            }
        }
        Math.max(0, 0)
        System.out.println(islands);
        return islands.size();  
    }
}

