class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        traced = set()
        visited = set()
        
        graph = collections.defaultdict(list)
        for des, sta in prerequisites:
            graph[sta].append(des)            

        def dfs(path):
            if path in traced:
                return False
            
            if path in visited:
                return True
            
            traced.add(path)
            
            for v in graph[path]:
                if not dfs(v):
                    return False

            traced.remove(path)
            visited.add(path)            
            
            return True
        
        for v in list(graph):
            if not dfs(v):
                return False
                

        return True