class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(left, right, turn):
            if left == right:
                if turn:
                    return [nums[left], 0]
                else:
                    return [0, nums[left]]
            if turn:
                leftScore = solve(left + 1, right, not turn)
                rightScore = solve(left, right - 1, not turn)
                leftScore[0] += nums[left]
                rightScore[0] += nums[right]
                if leftScore[0] - leftScore[1] > rightScore[0] - rightScore[1]:
                    return leftScore
                else:
                    return rightScore
            else:
                leftScore = solve(left + 1, right, not turn)
                rightScore = solve(left, right - 1, not turn)
                leftScore[1] += nums[left]
                rightScore[1] += nums[right]
                if leftScore[1] - leftScore[0] > rightScore[1] - rightScore[0]:
                    return leftScore
                else:
                    return rightScore

        ans = solve(0, len(nums) - 1, True)
        return ans[0] >= ans[1]