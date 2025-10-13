class Solution:
    def thousandSeparator(self, n: int) -> str:
        count = 0
        word = ''
        if n == 0:
            return '0'
        while n > 0:
            count += 1
            if count == 4:
                word += '.'
                count = 1
            word += str(n % 10)
            n //= 10
        return word[::-1]