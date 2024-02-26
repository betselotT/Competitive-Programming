class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        first = 1
        if n == first:
            return True
        if n < 3:
            return False
        return self.isPowerOfThree(n / 3) 
        