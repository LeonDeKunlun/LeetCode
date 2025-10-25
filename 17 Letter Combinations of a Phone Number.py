from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        digit_letters = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }

        letters = (digit_letters[digit] for digit in digits)
        results = [''.join(comb) for comb in product(*letters)]
        return results
