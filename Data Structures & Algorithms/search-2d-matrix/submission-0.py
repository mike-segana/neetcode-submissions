class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numColumns = len(matrix[0]) #x
        numRows = len(matrix) #y
        #treating matrix as 1d 0-indexed array
        left = 0
        right = numRows * numColumns - 1
        while left <= right:
            midpoint = left + ((right - left) // 2)
            col = midpoint % numColumns
            row = midpoint // numColumns
            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                left = midpoint + 1
            else:
                right = midpoint - 1
        return False