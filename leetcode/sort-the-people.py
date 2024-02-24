class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        newArr = {}
        arr = []
        for i in range(len(names)):
            newArr[heights[i]] = names[i]
        new = sorted(newArr.keys(), reverse=True)
        for key in new:
            arr.append(newArr[key])
        return arr