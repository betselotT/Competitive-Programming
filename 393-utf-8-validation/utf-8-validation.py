class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        expected_next_bytes = 0
        i = 0
        while i < n:
            if expected_next_bytes > 0:
                if (data[i] & 0b1100_0000) != 0b1000_0000:
                    return False
                expected_next_bytes -= 1
            else:
                if (data[i] & 0b1111_1000) == 0b1111_0000:
                    expected_next_bytes = 3
                elif (data[i] & 0b1111_0000) == 0b1110_0000:
                    expected_next_bytes = 2
                elif (data[i] & 0b1110_0000) == 0b1100_0000:
                    expected_next_bytes = 1
                elif (data[i] & 0b1000_0000) != 0:
                    return False
            i += 1
        return expected_next_bytes == 0