class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(2, n+1):
            x, y = y, x + y
            print('x: ',x, 'y: ', y)
        result = y if n >= 2 else n
        print(result)
        return result