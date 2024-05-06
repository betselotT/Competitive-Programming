class Solution:
    def getSum(self, a: int, b: int) -> int:
        bit = 0xffffffff
        while (b & bit) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        
        if b > 0:
            return a & bit
        else:
            return a