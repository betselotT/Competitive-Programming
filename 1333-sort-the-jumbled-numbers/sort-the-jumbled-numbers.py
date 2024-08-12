class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        dic = defaultdict()
        for i in range(len(mapping)):
            dic[i] = mapping[i]
        
        mapped = []
        for i in range(len(nums)):
            s = list(str(nums[i]))
            map = []
            for j in range(len(s)):
                n = int(s[j])
                map.append(str(dic[n]))
            mapped.append((int(''.join(map)),i))
        
        mapped.sort()
        
        ans= []
        for i in range(len(mapped)):
            ans.append(nums[mapped[i][1]])
            
        return ans