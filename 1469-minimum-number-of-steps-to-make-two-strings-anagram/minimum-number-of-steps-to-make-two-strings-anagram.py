class Solution(object):
    def minSteps(self, s, t):
        dicttS = Counter(s)
        dicttT = Counter(t)
        
        steps = 0
        
        for char in dicttS:
            if dicttS[char] > dicttT[char]:
                steps += dicttS[char] - dicttT[char]
        
        return steps
        
