class Solution:
    def binaryGap(self, n: int) -> int:
        s = str(bin(n))[2:]
        
        left = s.index('1')
        temp, max_dist = 1, 0

        for i in range(left + 1, len(s)):
            if s[i] == '1':
                if temp > max_dist:
                    max_dist = temp
                left, temp = i, 1
                continue
            temp += 1
        return max_dist