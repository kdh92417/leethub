class Solution:
    def binaryGap(self, n: int) -> int:
        bin_list = collections.deque(list(map(int, bin(n)[2:])))
        stack = []
        count = 1
        max_count = []
        while len(bin_list) > 0:
            cur = bin_list.popleft()
            if cur == 1 and cur not in stack:
                stack.append(cur)
            elif cur == 0 and 1 in stack:
                count += 1
            elif cur == 1 and cur in stack:
                max_count.append(count)
                count = 1



        return 0 if max_count == [] else max(max_count)