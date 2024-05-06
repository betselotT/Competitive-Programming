class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        parent = list(range(n))

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        
        def union(a, b):
            parent[find(a)] = find(b)
        
        for a, b in pairs:
            union(a, b)
        
        groups_i = defaultdict(list)
        groups_ch = defaultdict(list)

        for i in range(n):
            group = find(i)
            groups_i[group].append(i)
            groups_ch[group].append(s[i])
        
        ans = [""] * n
        for g in groups_i.keys():
            index = sorted(groups_i[g])
            chr = sorted(groups_ch[g])
            for i, c in zip(index, chr):
                ans[i] = c
        
        return "".join(ans)