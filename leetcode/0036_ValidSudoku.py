from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in board:
            s = set()
            for item in row:
                if item == ".":
                    continue
                if item in s:
                    return False
                s.add(item)

        # check column
        for i in range(9):
            s = set()
            for row in board:
                item = row[i]
                if item == ".":
                    continue
                if item in s:
                    return False
                s.add(item)

        # check 3x3
        for i in range(3):
            for j in range(3):
                s = set()
                for k in range(3):
                    for l in range(3):
                        item = board[i * 3 + k][j * 3 + l]
                        if item == ".":
                            continue
                        if item in s:
                            return False
                        s.add(item)

        return True


if __name__ == "__main__":
    solution = Solution()
    board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                           ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    assert solution.isValidSudoku(board1) == True

    board2 = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                           ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    assert solution.isValidSudoku(board2) == False
