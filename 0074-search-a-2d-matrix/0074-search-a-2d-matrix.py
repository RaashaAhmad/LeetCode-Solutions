class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        #Brute Force Solution
        '''
        for r in range(0 , rowLen):
            for c in range(0, colLen):
                if matrix[r][c] == target:
                    return True
        return False
        '''
        #Binary Search
        l = 0
        r = (rowLen * colLen) - 1
        while l <= r:
            m = l + (r - l) // 2
            row = m // colLen
            col = m % colLen
            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
            else:
                return True
        return False