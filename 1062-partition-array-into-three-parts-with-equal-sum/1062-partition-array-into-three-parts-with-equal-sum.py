class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        n = len(arr)
        
        if total_sum % 3 != 0:
            return False
        
        target_sum = total_sum // 3
        current_sum = 0
        partitions_found = 0
        
        for i in range(n):
            current_sum += arr[i]
            if current_sum == target_sum:
                partitions_found += 1
                current_sum = 0 
                
            if partitions_found == 2 and i < n - 1:
                return True
        
        return False

        