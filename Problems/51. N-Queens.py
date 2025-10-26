class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        results = list()

        Q_rows = [f"{'.' * col}Q{'.' * (n-col-1)}" for col in range(n)]
        columns = set()
        pos_diags = set()
        neg_diags = set()
        def backtrack(path, row):
            if row == n:
                results.append(path.copy())
                return

            for col in range(n):
                if col not in columns and (row - col) not in pos_diags and (row + col) not in neg_diags:
                    path[row] = Q_rows[col]
                    columns.add(col)
                    pos_diags.add(row - col)
                    neg_diags.add(row + col)

                    backtrack(path, row+1)

                    columns.remove(col)
                    pos_diags.remove(row - col)
                    neg_diags.remove(row + col)

        backtrack([''] * n, 0)
        return results
