class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        mapp = {}
        res = []

        for i in pieces:
            mapp[i[0]] = i

        for i in arr:
            if i in mapp:
                res += mapp[i]
        
        return res == arr