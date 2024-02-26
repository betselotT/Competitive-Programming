MOD = 10**9 + 7
class Solution:
    def new(self, num1, pow):
        print(pow)
        if pow == 1:
            return num1
        if pow <= 0:
            return 1
        elif pow % 2 == 0:
            return (self.new(num1, pow // 2)**2) % MOD
        else:
            return (num1 * self.new(num1, (pow - 1) // 2)**2) % MOD

    def countGoodNumbers(self, n: int) -> int:
        po = ceil(n / 2)
        poo = n // 2
        return (self.new(5, po) * self.new(4, poo)) % MOD
        