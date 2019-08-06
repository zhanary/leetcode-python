class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dic = set()
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr != '.':
                    if (i, curr) in dic or (curr, j) in dic or (i/3, j/3, curr) in dic:
                        return False
                    dic.add((i, curr))
                    dic.add((curr, j))
                    dic.add((i/3, j/3, curr))
        return True
