class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows , columns , boxes = defaultdict(set) , defaultdict(set) , defaultdict(set)

        for i in range(9):
            for j in range(9):
                
                if board[i][j] == '.':
                    continue
                if board[i][j] not in rows[i] and board[i][j] not in columns[j] and board[i][j] not in boxes[(i // 3, j // 3)]:
                    rows[i].add(board[i][j])
                    
                    columns[j].add(board[i][j])
                    
                    boxes[(i // 3, j // 3)].add(board[i][j])                
                else:
                    return False

        return True
