class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for i in range(len(operations)):
            if operations[i] == "+":
                num = arr[-1] + arr[-2]
                arr.append(num)
            elif operations[i] == "D":
                num = 2 * arr[-1]
                arr.append(num)
            elif operations[i] == "C":
                arr.pop()
            else:
                arr.append(int(operations[i]))
        
        return sum(arr)