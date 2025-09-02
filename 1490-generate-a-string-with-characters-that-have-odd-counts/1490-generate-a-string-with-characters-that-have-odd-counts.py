class Solution:
    def generateTheString(self, n: int) -> str:
        s=""
        if n%2==0:
            s+=(n-1)*"a"
            s+="b"
        else:
            s+=n*"a"
        return s

        