class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        result = []
        
        for num in nums:
            prev += num
            result.append(prev)
            
        return result