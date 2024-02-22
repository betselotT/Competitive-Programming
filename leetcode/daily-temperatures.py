class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        myDict = defaultdict(int)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j, num = stack.pop() 
                myDict[j] = i - j
            stack.append((i, temp))
        ans = []
        for i in range(len(temperatures)):
            ans.append(myDict[i])
        return ans