class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) -1
        while left < right:
            mid = (left + (right - left) // 2)
            print(nums[mid], mid, 'left: ', left, ' right: ', right)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        pivot = left
        left, right = 0, len(nums) -1
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (pivot + mid) % len(nums)
            
            if nums[mid_pivot] > target:
                right = mid -1
            elif nums[mid_pivot] < target:
                left = mid +1
            else:
                return mid_pivot
        return -1
        
        