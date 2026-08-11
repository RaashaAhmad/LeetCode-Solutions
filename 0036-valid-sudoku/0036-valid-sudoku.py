class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Brute Force Solution
        '''for i in range(9):
            rowSeen = set()
            colSeen = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rowSeen:
                    return False
                rowSeen.add(board[i][j])
                if board[j][i] == '.':
                    continue
                if board[j][i] in colSeen:
                    return False
                colSeen.add(board[j][i])
        for square in range(9):
            squareSeen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 +j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in squareSeen:
                        return False
                    squareSeen.add(board[row][col])
        return True'''
        #Hash Map Solution
        rowSeen = defaultdict(set)
        colSeen = defaultdict(set)
        squareSeen = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if (board[row][col] in rowSeen[row] or
                board[row][col] in colSeen[col] or
                board[row][col] in squareSeen[(row // 3, col // 3)]):
                    return False
                rowSeen[row].add(board[row][col])
                colSeen[col].add(board[row][col])
                squareSeen[(row // 3, col // 3)].add(board[row][col])
        return True