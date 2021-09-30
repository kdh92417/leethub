class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0 for _ in range(numCourses)]
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        
        def dfs(x):
            
            if visited[x] == -1:
                return False
            elif visited[x] == 1:
                return True
            
            visited[x] = -1
            for y in graph[x]:
                if not dfs(y):
                    return False
            visited[x] = 1
        
            return True
        
        for y in list(graph):
            if not dfs(y):
                return False
        
        return True