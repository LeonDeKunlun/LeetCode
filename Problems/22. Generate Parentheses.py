from itertools import product

class Solution:
    parenthesis = {0: ['']}

    def generateParenthesis(self, n: int) -> list[str]:

        def get_parenthesis(n):
            if n in Solution.parenthesis:
                return Solution.parenthesis[n]

            result = list()
            for i in range(1, n+1):
                result_iter = product(
                    (f'({p})' for p in get_parenthesis(i-1)),
                    get_parenthesis(n-i),
                )
                result.extend(''.join(p) for p in result_iter)
            Solution.parenthesis[n] = result
            return result

        return get_parenthesis(n).copy()
