class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = [[] for _ in range(numRows)]
        row, turn, down = 0, 0, True
        for i, e in enumerate(s):
            res[row].append(e)
            row = row + 1 if down else row - 1
            if abs(row - turn) + 1 == numRows:
                down, turn = not down, row
        return "".join("".join(e) for e in res)
