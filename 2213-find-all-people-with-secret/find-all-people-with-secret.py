class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]

    def get(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.get(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.get(x)
        parent_y = self.get(y)
        if parent_x != parent_y:
            if self.size[parent_x] >= self.size[parent_y]:
                self.parent[parent_y] = parent_x
                self.size[parent_x] += self.size[parent_y]
            else:
                self.parent[parent_x] = parent_y
                self.size[parent_y] += self.size[parent_x]
                
    def is_connected(self, x, y):
        parent_x = self.get(x)
        parent_y = self.get(y)

        return parent_x == parent_y

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x :x[2])
        ans = []
        
        union_find = UnionFind(n)
        union_find.union(0,firstPerson)
        
        i = 0
        while i < len(meetings):
            p1,p2,time = meetings[i][0], meetings[i][1], meetings[i][2]
            curr = []
            flag = False
            inn = False
            while i < len(meetings) and time == meetings[i][2]:
                inn = True
                t1,t2 = meetings[i][0], meetings[i][1]
                union_find.union(t1,t2)
                curr.extend([t1,t2])
                i += 1
           
            for c in curr:
                if not union_find.is_connected(0,c):
                    union_find.parent[c] = c
            
            if not inn:
                i += 1


       
        for c in range(n+1):
            if union_find.is_connected(0,c):
                ans.append(c)

        return ans