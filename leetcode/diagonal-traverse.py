class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
            myDict = {}
            newArr = []

            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i+j in myDict:
                       myDict[i+j].append(mat[i][j])
                    else:
                        myDict[i+j] = [mat[i][j]]
            for i, j in myDict.items():
                if i % 2 == 0:
                    j.reverse()
                    newArr.extend(j)
                else:
                    newArr.extend(j)
                    
            return newArr 
