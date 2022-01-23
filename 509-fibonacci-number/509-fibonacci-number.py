class Solution:
    def fib(self, n: int) -> int:
        nums = [0, 1]
        
        if n < 2:
            return nums[n]
        
        while len(nums) <= n:
            nums.append(nums[-1] + nums[-2])
            
        return nums[-1]
        
        
    