class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []
        
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                letters.append(char)
        
        if abs(len(letters) - len(digits)) > 1:
            return ""
        
        result = []
        if len(letters) > len(digits):
            long_list, short_list = letters, digits
        else:
            long_list, short_list = digits, letters
        
        for i in range(len(long_list)):
            result.append(long_list[i])
            if i < len(short_list):
                result.append(short_list[i])
        
        return ''.join(result)