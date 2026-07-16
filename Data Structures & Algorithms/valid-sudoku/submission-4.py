class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for y in range(len(board)):
            seen = set()
            for x in range(len(board)):
                if board[y][x] in seen:
                    return False
                else:
                    if board[y][x] != ".":
                        seen.add(board[y][x])
        # Check cols
        for y in range(len(board)):
            seen = set()
            for x in range(len(board)):
                if board[x][y] in seen:
                    return False
                else:
                    if board[x][y] != ".":
                        seen.add(board[x][y])
        
        # Check 3x3 squares
        for y in range(0, len(board), len(board) // 3):
            for x in range(0, len(board), len(board) // 3):
                seen = set()
                for yy in range(y, y + (len(board) // 3)):
                    for xx in range(x, x + (len(board) // 3)):
                        if board[yy][xx] in seen:
                            return False
                        else:
                            if board[yy][xx] != ".":
                                seen.add(board[yy][xx])
        return True