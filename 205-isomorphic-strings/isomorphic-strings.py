class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}
        
        for ss, tt in zip(s, t):
            if ss in st:
                if st[ss] != tt:
                    return False
            else:
                st[ss] = tt
            
            if tt in ts:
                if ts[tt] != ss:
                    return False
            else:
                ts[tt] = ss
        
        return True