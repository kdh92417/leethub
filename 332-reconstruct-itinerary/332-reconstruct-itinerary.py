class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        path = collections.defaultdict(list)
        for sta, des in sorted(tickets, reverse=True):
            path[sta].append(des)
            
        route = collections.deque()
        def dfs(v):      
            while path[v]:
                dfs(path[v].pop())

            route.appendleft(v)
            
        dfs('JFK')
        
        return route
        
        