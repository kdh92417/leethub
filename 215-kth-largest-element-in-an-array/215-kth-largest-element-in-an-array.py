class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        
        for num in nums:
            heapq.heappush(h, -num)
        
        for _ in range(k):
            result = -heapq.heappop(h)
            
        return result
        
        