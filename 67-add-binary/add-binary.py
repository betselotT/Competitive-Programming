class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)
        num = a + b
        num = bin(num)
        return num[2:]