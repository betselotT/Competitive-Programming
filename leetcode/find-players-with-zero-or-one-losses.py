class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        arrWin = []
        ans = []
        setSecond = set()
        oneLose = defaultdict(int)
        lose = []
        for i in range(len(matches)):
            oneLose[matches[i][1]] += 1
            oneLose[matches[i][0]] += 0
        for key, value in oneLose.items():
            if value == 1:
                lose.append(key) 
            elif value == 0:
                arrWin.append(key)
            
        arrWin.sort()
        lose.sort()
        ans.append(arrWin)
        ans.extend([lose])
        return ans