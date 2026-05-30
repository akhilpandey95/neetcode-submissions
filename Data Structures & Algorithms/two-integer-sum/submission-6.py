class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) >= 2 and len(nums) <= 1000:
            solutions = {}

            for idx, num in enumerate(nums):
                solutions[num] = idx

            for idx, num in enumerate(nums):
                diff = target - num
                if diff in solutions and solutions[diff] != idx:
                    return [idx, solutions[diff]]

            return []

            # for num_i in range(0, len(nums) - 1):
            #     for num_j in range(1, len(nums)):
            #         if nums[num_i] + nums[num_j] == target and num_i != num_j:
            #             return [num_i, num_j]

