class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heapq.heapify(people)
        result = [None] * len(people)

        while people:
            p = heapq.heappop(people)
            value, order = p

            for i in range(len(result)):
                if result[i] is None and order == 0:
                    result[i] = p
                    break

                if result[i] is None or (result[i] and result[i][0] >= value):
                    order -= 1
        return result
        