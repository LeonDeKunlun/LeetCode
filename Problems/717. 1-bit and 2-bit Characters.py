class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = len(bits) - 2
        while i >= 0:
            if bits[i] == 0:
                return True
            if i-1 < 0 or bits[i-1] == 0:
                return False
            i -= 2
        return True