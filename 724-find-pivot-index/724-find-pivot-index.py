class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        
        for idx, num in enumerate(nums):
            if idx != 0:
                left += nums[idx - 1]
            right -= num
            if left == right:
                return idx
        else:
            return -1