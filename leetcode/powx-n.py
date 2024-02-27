class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, (n * -1))
        elif n % 2 != 0:
            return x * self.myPow(x, n - 1)
        else:
            result = self.myPow(x, n // 2)
            return result * result