class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # Make the graph
        graph = collections.defaultdict(list)
        for dep, arr in sorted(tickets):
            graph[dep].append(arr)
        
        # Path
        route = []
        
        # DFS
        def dfs(a):    
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
            
        dfs('JFK')
            
        return route[::-1]
        
        