class Solution:
    def longestPalindrome(self, s: str) -> int:
        myDict = Counter(s)
        count = 0
        isOdd = False
        for key, value in myDict.items():
            if value % 2 == 0:
                count += value
            else:
                isOdd = True
                count += value - 1
        if not isOdd:
            return count
        else:
            return count + 1
                