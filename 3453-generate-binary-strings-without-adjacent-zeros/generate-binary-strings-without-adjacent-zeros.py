class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        k1 = "0"
        k2 = "1"
        
        if n == 1:
            ans.append(k1)
            ans.append(k2)
            return ans
        
        k = (1 << n)
        
        for i in range(1, k):
            s = ""
            for j in range(n - 1, -1, -1):
                if ((i >> j) & 1) == 1:
                    s += '1'
                else:
                    s += '0'
            
            isValid = True
            for j in range(n - 1):
                if s[j] == '0' and s[j + 1] == '0':
                    isValid = False
                    break
            
            if isValid:
                ans.append(s)
        
        return ans