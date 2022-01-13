class Solution:
    def search(self, nums: List[int], target: int) -> int:
  
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx <= right_idx:
            mid = (left_idx + right_idx) // 2
            if nums[mid] > target:
                right_idx = mid - 1
            elif nums[mid] < target:
                left_idx = mid + 1
            else:
                return mid
            
        return -1