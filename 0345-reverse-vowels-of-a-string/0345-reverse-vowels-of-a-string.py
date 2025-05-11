class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        n = len(s)
        j = n-1
        vowels = set("aeiouAEIOU")
        # print(vowels)
        while(i<j):
            if s[i] in vowels and s[j] in vowels:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1

            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1

        return "".join(s)