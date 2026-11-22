class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i, v in enumerate(nums):
            if v in nums[i+1:]:
                return True
        return False