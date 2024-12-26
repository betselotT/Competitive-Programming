class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def _convertInt(nums):
            s = 0
            for n in nums:
                n = ord(n) - 48
                s = s * 10 + n
            return s
        num1 = _convertInt(num1)
        num2 = _convertInt(num2)
        num = num1 + num2
        if num == 0:
            return "0"
        def _convertStr(num):
            st = ""
            while num > 0:
                n = num % 10
                n = chr(n + 48)
                st = n + st
                num //= 10
            return st
        st = _convertStr(num)
        return st