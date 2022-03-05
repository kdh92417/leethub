class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        path = collections.defaultdict(list)
        for sta, des in sorted(tickets):
            path[sta].append(des)
            
        route, stack = [], ['JFK']
        
        while stack:
            
            while path[stack[-1]]:
                stack.append(path[stack[-1]].pop(0))
            route.append(stack.pop())        
        
        return route[::-1]
        
        