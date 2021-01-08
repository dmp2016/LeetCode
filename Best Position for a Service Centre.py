from typing import List
import math


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        if len(positions) == 1:
            return 0
        def fun(x, y):
            return sum([math.sqrt(math.pow(x - xi, 2) + math.pow(y - yi, 2)) for xi, yi in positions])

        def grad(x, y):
            return (sum([(x - xi)/(math.sqrt(math.pow(x - xi, 2) + math.pow(y - yi, 2))) if abs(x - xi) > 0.000001 else 0 for xi, yi in positions]), 
                    sum([(y - yi)/(math.sqrt(math.pow(x - xi, 2) + math.pow(y - yi, 2))) if abs(y - yi) > 0.000001 else 0 for xi, yi in positions]))
        
        x0 = sum([xi for xi, _ in positions])/len(positions)
        y0 = sum([yi for _, yi in positions])/len(positions)
        L = 1
        while True:
            vec = grad(x0, y0)
            # vec_norm = math.sqrt(math.pow(vec[0], 2) + math.pow(vec[1], 2))
            old_val = fun(x0, y0)
            x0, y0 = x0 - vec[0]*L, y0 - vec[1]*L
            new_val = fun(x0, y0)
            if new_val > old_val:
                L /= 5
                continue
            if old_val - new_val < 0.000001:
                return new_val

    def getMinDistSum1(self, positions: List[List[int]]) -> float:

        def fun(x, y):
            return sum([math.sqrt(math.pow(x - xi, 2) + math.pow(y - yi, 2)) for xi, yi in positions])

        x0, y0 = 50, 50
        val0 = fun(x0, y0)
        step_size = 1
        steps = [10, 10, 10, 10, 10, 10, 10]
        sizes = [10, 1, 0.1, 0.01, 0.01, 0.001, 0.0001]

        for step, step_size in zip(steps[:-1], sizes[:-1]):
            x = x0 - step_size * step
            y1 = y0 - step_size * step
            for _ in range(2 * step + 1):
                y = y1
                for _ in range(2 * step + 1):
                    val = fun(x, y)
                    if val < val0:
                        val0 = val
                        x0, y0 = x, y
                    y += step_size
                x += step_size
        return val0

test = Solution()
print(test.getMinDistSum([[0,1],[1,0],[1,2],[2,1]]))
print(test.getMinDistSum(positions = [[1,1],[3,3]]))
print(test.getMinDistSum(positions = [[1,1]]))
print(test.getMinDistSum(positions = [[1,1],[0,0],[2,0]]))
print(test.getMinDistSum(positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]))
print(test.getMinDistSum([[0,1],[1,0],[1,2],[2,1],[1,1]]))
print(test.getMinDistSum([[88,76],[21,33],[19,30],[35,32],[19,30],[84,80],[77,65],[30,16],[33,17],[19,27],[72,68],[23,36],[16,21],[67,69],[34,33],[85,78],[29,37],[24,18],[83,71],[79,74],[36,23],[94,64],[24,20],[71,80],[88,77],[21,16],[35,20],[90,78],[86,71],[79,65],[24,21]]))
print(test.getMinDistSum([[19,40],[12,31],[84,92],[67,60],[20,94],[6,13],[13,82],[7,31],[82,87],[0,51],[90,77],[60,17],[13,33],[45,45],[60,42],[62,62],[51,59],[74,5],[15,16],[55,95],[0,23],[34,26],[1,90],[70,12],[43,44],[87,7],[62,4],[22,1],[54,9],[18,39],[59,58],[16,57]]))
print(test.getMinDistSum([[92,93],[54,54],[61,54],[60,56],[53,58],[53,53],[91,92],[91,91],[92,92],[60,57],[92,92],[92,91],[93,91],[59,52],[93,91],[92,92],[92,92],[93,91],[92,92],[61,52],[61,57],[57,52],[61,54],[52,52],[93,93],[52,56],[57,54],[52,58],[93,93],[93,93],[92,93],[91,91]]))
print(test.getMinDistSum1([[92,93],[54,54],[61,54],[60,56],[53,58],[53,53],[91,92],[91,91],[92,92],[60,57],[92,92],[92,91],[93,91],[59,52],[93,91],[92,92],[92,92],[93,91],[92,92],[61,52],[61,57],[57,52],[61,54],[52,52],[93,93],[52,56],[57,54],[52,58],[93,93],[93,93],[92,93],[91,91]]))
print(test.getMinDistSum([[44,23],[18,45],[6,73],[0,76],[10,50],[30,7],[92,59],[44,59],[79,45],[69,37],[66,63],[10,78],[88,80],[44,87]]))
print(test.getMinDistSum([[16,56],[4,87],[80,26],[76,68],[89,23],[8,55]]))
print(test.getMinDistSum([[55,91],[83,86],[48,8],[71,31],[50,28],[28,52],[89,18],[61,5],[100,100],[63,94],[93,49],[82,72],[17,9],[63,48],[83,96],[47,2],[43,50],[95,32],[87,74],[39,80],[57,15],[98,95],[37,53]]))
