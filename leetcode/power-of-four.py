class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        first = 1
        if n == first:
            return True
        if n < 4:
            return False
        return self.isPowerOfFour(n / 4) 