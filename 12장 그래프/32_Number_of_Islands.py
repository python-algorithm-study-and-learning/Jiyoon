class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x: int, y: int) -> None:
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == "1":
                grid[x][y] = "0"
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
            
            return None
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        return cnt
                    
