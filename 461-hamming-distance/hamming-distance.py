class Solution:
    def hammingDistance(self,x,y):
        num = x ^ y
        a = bin(num)
        ans = a.count('1')
        return ans