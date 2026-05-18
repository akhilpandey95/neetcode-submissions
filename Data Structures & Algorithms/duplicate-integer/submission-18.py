class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) >= 0 and len(nums) <= 10**5:
            set_nums = list(set(nums))

            if len(set_nums) != len(nums):
                return True

        return False
