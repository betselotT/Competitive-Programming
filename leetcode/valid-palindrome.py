class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower()
        arr = []
        for i in low:
            if i.isalnum() == True:
                arr.append(i) 
        ans = "".join(arr)
        left, right = 0, len(ans) - 1
        for _ in range(len(ans)):
            if ans[left] != ans[right]:
                return False
            left += 1
            right -= 1
        return True