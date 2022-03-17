class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        result = []
        graph = collections.defaultdict(list)
        
        for sta, des in sorted(tickets, reverse=True):
            graph[sta].append(des)
        
        def dfs(path):
            
            while graph[path]:
                dfs(graph[path].pop())
            result.append(path)
        
        dfs('JFK')
        
        return result[::-1]