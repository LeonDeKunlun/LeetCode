class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l_index = 0
        r_index = m * n - 1
        while l_index <= r_index:
            m_index = (l_index + r_index) >> 1
            i, j = divmod(m_index, n)
            mid = matrix[i][j]
            if mid == target:
                return True
            elif mid < target:
                l_index = m_index + 1
            else:
                r_index = m_index - 1
        return False
