from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        hind = list(enumerate(height))
        hind.sort(key=lambda x: x[1])
        inds = [True for _ in range(len(height))]
        min_ind = 0
        max_ind = len(height) - 1
        max_s = 0
        for hi in hind[:-1]:
            ind, h = hi[0], hi[1]
            w = max(ind - min_ind, max_ind - ind)
            max_s = max(h * w, max_s)
            inds[ind] = False
            while not inds[min_ind]:
                min_ind += 1
            while not inds[max_ind]:
                max_ind -= 1
        return max_s


test = Solution()
print(test.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
height = [1, 1]
print(test.maxArea(height))

height = [4, 3, 2, 1, 4]
print(test.maxArea(height))

height = [1, 2, 1]
print(test.maxArea(height))
