import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue
                box = boxes[math.floor(i/3)][math.floor(j/3)]
                if cell in rows[i] or cell in columns[j] or cell in box:
                    return False

                rows[i].add(cell)
                columns[j].add(cell)
                box.add(cell)

        return True