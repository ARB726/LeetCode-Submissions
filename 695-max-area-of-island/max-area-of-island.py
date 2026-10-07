class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        Rows , Columns  = len(grid) , len(grid[0])
        
        maxArea = 0

        Cordinates = [[1,0],[0,1],[-1,0],[0,-1]]

        hashSet = set()


        def bfs(r,c):
            queue = deque([(r,c)])
            hashSet.add((r,c)) # add a tuple
            area = 0
            while queue:
                row , col = queue.popleft()
                area +=1

                for dr , dc in Cordinates: # direction of row and column
                    nr , nc = dr + row , dc + col

                    if 0 <= nr < Rows and 0 <= nc < Columns and grid[nr][nc] == 1 and (nr,nc) not in hashSet:
                        queue.append((nr,nc))
                        hashSet.add((nr,nc))
            
            return area

        for r in range(Rows):
            for c in range(Columns):


                if grid[r][c] == 1 and (r,c) not in hashSet:
                    area = bfs(r,c)
                    maxArea = max(area,maxArea)
        
        return maxArea

