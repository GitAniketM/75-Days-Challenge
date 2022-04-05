class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def dfs(i, j, n, m, grid):
            if i < 0 or j < 0 or i >=n or j >= m or grid[i][j] == 0 :
                return 0
            
            grid[i][j] = 0
            return 1 + dfs(i-1,j,n,m,grid) + dfs(i+1,j,n,m,grid) + dfs(i,j+1,n,m,grid) + dfs(i,j-1,n,m,grid)
        
        
        n = len(grid)
        m = len(grid[0])
        maxi = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxi = max(maxi, dfs(i,j,n,m,grid))
                    
        return maxi