from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        if not arr:
            return True
        inds = {}
        for ind in range(len(arr)):
            inds[arr[ind]] = ind
        cov_len = 0
        for ind in range(len(pieces)):
            if pieces[ind] and pieces[ind][0] in inds:
                st = inds[pieces[ind][0]]
                if arr[st:st + len(pieces[ind])] == pieces[ind]:
                    cov_len += len(pieces[ind])
                    if cov_len == len(arr):
                        return True
        return False


test = Solution()
print(test.canFormArray(arr = [85], pieces = [[85]]))
print(test.canFormArray(arr = [15,88], pieces = [[88],[15]]))
print(test.canFormArray(arr = [49,18,16], pieces = [[16,18,49]]))
print(test.canFormArray(arr = [91,4,64,78], pieces = [[78],[4,64],[91]]))
print(test.canFormArray(arr = [1,3,5,7], pieces = [[2,4,6,8]]))
