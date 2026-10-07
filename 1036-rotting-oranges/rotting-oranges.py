class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        Rows , Columns  = len(grid) , len(grid[0]) 
        Directions = [[0,1],[1,0],[-1,0],[0,-1]]
        fresh = 0
        queue = deque()

        for r in range(Rows):
            
            for c in range(Columns):
                
                if grid[r][c] == 1:

                    fresh +=1

                elif grid[r][c] ==2:

                    queue.append((r,c,0))
        
        minTaken = 0
        while queue:

            r,  c,  mins = queue.popleft()

            for dr , dc in Directions:

                nr , nc = dr + r , dc + c

                if 0 <= nr < Rows and 0 <= nc < Columns and grid[nr][nc] == 1:

                    fresh -=1
                    grid[nr][nc] = 2
                    minTaken = mins + 1

                    queue.append((nr,nc,minTaken))


        if fresh != 0: return -1

        else: return minTaken
        
