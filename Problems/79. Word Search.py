from collections import Counter
from itertools import chain

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_len = len(word)

        if m * n < word_len:
            return False

        word_cnt = Counter(word)
        board_cnt = Counter(chain.from_iterable(board))

        if not board_cnt >= word_cnt:
            return False

        least_letter = min((cnt, letter) for letter, cnt in board_cnt.items() if letter in word_cnt)[1]
        least_index = word.index(least_letter)

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1),]
        def backtrack(coord, word, index, visited=None):
            if visited is None:
                visited = set()

            i, j = coord
            if i < 0 or i >= m or j < 0 or j >= n or coord in visited:
                return False

            if board[i][j] != word[index]:
                return False

            if index == word_len - 1:
                return True

            visited.add(coord)
            indicator = any(backtrack((i+x, j+y), word, index+1, visited) for x, y in directions)
            visited.remove(coord)
            return indicator

        for i, boardi in enumerate(board):
            for j, letter in enumerate(boardi):
                if letter == least_letter:
                    if backtrack((i, j), word, least_index) and backtrack((i, j), word[:: -1], word_len - 1 - least_index):
                        return True
        return False
