class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            
            for task, _ in count.most_common(n + 1):
                sub_count += 1
                result += 1
                
                count.subtract(task)
                count += collections.Counter()
                
            if not count:
                break
            
            result += n - sub_count + 1
        return result