from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:        
        if not height:
            return 0
        res = 0
        hind = list(enumerate(height))
        hind.sort(key=lambda x: -x[1])
        cur_left = hind[0][0]
        cur_right = cur_left
        for i in range(1, len(hind)):
            new_ind = hind[i][0]
            if new_ind > cur_right:
                for j in range(cur_right + 1, new_ind):
                    res += height[new_ind] - height[j]
                cur_right = new_ind
            if new_ind < cur_left:
                for j in range(new_ind + 1, cur_left):
                    res += height[new_ind] - height[j]
                cur_left = new_ind
        return res


test = Solution()
print(test.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(test.trap(height = [4,2,0,3,2,5]))
