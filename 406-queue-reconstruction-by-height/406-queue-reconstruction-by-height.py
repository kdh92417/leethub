class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        result = []
        
        for p in people:
            heapq.heappush(heap, [-p[0], p[1]])
            
        while heap:
            p = heapq.heappop(heap)
            result.insert(p[1], [-p[0], p[1]])

        return result
