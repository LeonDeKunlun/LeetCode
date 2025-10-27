class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = [0] * n

        num = 1
        n_tenths = n // 10
        for i in range(n):
            result[i] = num

            if num <= n_tenths:
                num *= 10
            else:
                if num >= n:
                    num //= 10
                while num % 10 == 9:
                    num //= 10
                num += 1

        return result
