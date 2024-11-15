class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        onerow=[]
        onecol=[]
        zerorow=[]
        zerocol=[]
        one=0
        zero=0
        for i in range (m):
            j=0
            while(j<n):
                if(grid[i][j]==0):
                    zero += 1
                else:
                    one += 1
                j += 1
            zerorow.append(zero)
            onerow.append(one)
            zero=0
            one=0
        zero = 0
        one = 0
        for j in range(n):
            i=0
            while(i<m):
                if(grid[i][j]==0):
                    zero+=1
                else:
                    one+=1
                i+=1
            zerocol.append(zero)
            onecol.append(one)
            zero=0
            one=0

        diff = [[0 for j in range(n)] for i in range(m)]

                
        for i in range(m):
            for j in range(n):
                diff[i][j] = onerow[i] + onecol[j] - zerorow[i] - zerocol[j]
        return diff