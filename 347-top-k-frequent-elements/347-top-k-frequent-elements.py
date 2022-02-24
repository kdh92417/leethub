class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c = collections.Counter(nums)
        
        result = sorted(c.items(), key=lambda x: x[1], reverse=True)[:k]
        
        return [key for key, value in result]
        