class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ordList = [ord(x)-97 for x in s]
        prefix = [0]*(len(s)+1)

        for i in range(len(shifts)):
            if shifts[i][2] == 1:
                prefix[shifts[i][0]] +=  1
                prefix[shifts[i][1]+1] -=  1
            else:
                prefix[shifts[i][0]] -= 1
                prefix[shifts[i][1]+1] += 1
        final = []
        prefix = list(accumulate(prefix))

        for i in range(len(ordList)):
            final.append(chr((ordList[i] + prefix[i]) % 26 + 97))
        return "".join(final)