class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_nums = []
        odd_nums = []
        my_list = []

        for i in nums:
            if i % 2 == 0:
                even_nums.append(i)
            else:
                odd_nums.append(i)

        for j in range(len(nums)):
            if j % 2 == 0:
                my_list.append(even_nums[j//2])
            else:
                my_list.append(odd_nums[j//2])

        return my_list

        