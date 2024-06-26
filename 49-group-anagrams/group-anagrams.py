class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            check = tuple(sorted(s))
            ans[check].append(s)
        
        return list(ans.values())