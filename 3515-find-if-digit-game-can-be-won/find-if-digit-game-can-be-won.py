class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        strNums = []
        for num in nums:
            strNums.append(str(num))
        countOne, countTwo = 0, 0
        for num in strNums:
            if len(num) == 1:
                countOne += int(num)
        for num in strNums:
            if len(num) == 2:
                countTwo += int(num)
        
        if countOne == countTwo:
            return False
        else:
            return True