class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c=0
        if not moves.count('U') == moves.count("D"):
            c+=1
        if not moves.count('L') == moves.count('R'):
            c+=1
        return c==0