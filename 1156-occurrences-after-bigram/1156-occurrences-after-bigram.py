class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_list = text.split()
        result = []
        
        for i in range(len(text_list) - 2):
            if text_list[i] == first and text_list[i + 1] == second:
                result.append(text_list[i + 2])
        
        return result