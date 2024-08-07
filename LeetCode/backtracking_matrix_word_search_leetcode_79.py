


from typing import List 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0]) 
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path
            ):
                return False
            path.add((r, c))
            res = (
                dfs(r+1, c, i+1) or 
                dfs(r-1, c, i+1) or 
                dfs(r, c+1, i+1) or 
                dfs(r, c-1, i+1)
            )
            path.remove((r, c))
            return res
        
        # First find out where in the matrix is the first character of the word
        rc_set = []
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    rc_set.append((r, c))
        for rc in rc_set:
            r = rc[0]
            c = rc[1]
            if dfs(r, c, 0):
                return True

        return False
