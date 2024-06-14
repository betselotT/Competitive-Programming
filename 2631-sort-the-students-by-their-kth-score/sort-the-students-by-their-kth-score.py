class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        myDict = {}
        arr = []

        for i in range(len(score)):
            arr.append(score[i][k])

        for j in range(len(score)):
            myDict[arr[j]]=score[j]

        for kk in sorted(myDict.keys(), reverse=True):
            ans.append(myDict[kk])
        
        return ans