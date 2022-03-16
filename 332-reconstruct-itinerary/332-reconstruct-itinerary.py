class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        result = []
        graph = collections.defaultdict(list)
        
        for sta, des in sorted(tickets, reverse=True):
            graph[sta].append(des)
        
        stack  = ['JFK']
        while stack:
            
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            result.append(stack.pop())
        
        return result[::-1]
        
        