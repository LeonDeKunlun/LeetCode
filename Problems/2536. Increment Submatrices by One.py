from itertools import accumulate, islice

class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        mat = [[0] * (n+1) for _ in range(n+1)]
        for row1, col1, row2, col2 in queries:
            mat[row1][col1] += 1
            mat[row2+1][col1] += -1
            mat[row1][col2+1] += -1
            mat[row2+1][col2+1] += 1

        def transposed_acc_cols(mat):
            return [list(accumulate(col)) for col in zip(*mat)]

        mat = (islice(row, n) for row in islice(mat, n))
        mat = transposed_acc_cols(transposed_acc_cols(mat))
        return mat
