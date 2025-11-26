from collections import deque
from itertools import repeat

class Solution:
    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        modulus = 1_000_000_007
        m, n = len(grid), len(grid[0])
        row_paths = [deque(repeat(0, k)) for _ in range(n+1)]
        row_paths[1][0] = 1
        for row in grid:
            for j, elem in enumerate(row, start=1):
                # update row_paths[j][(r+elem) % k] to row_paths[j-1][r] + row_paths[j][r]
                elem_paths = row_paths[j]
                for value in row_paths[j-1]:
                    path = elem_paths.popleft() + value
                    elem_paths.append(path if path < modulus else path - modulus)
                elem_paths.rotate(elem % k)
        return row_paths[-1][0] % modulus