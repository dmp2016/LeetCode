from bisect import bisect_left, bisect_right


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        nums0 = [nums[ind] for ind in range(0, len(nums) - 4) if nums[ind] != nums[ind + 4]]
        nums0 += nums[-4:]
        nums = nums0
        ind_a_min = bisect_left(nums, target - nums[-1] - nums[-2] - nums[-3], 0, len(nums) - 4)
        nums4 = [nums[ind] + nums[ind + 1] + nums[ind + 2] + nums[ind + 3] for ind in range(0, len(nums) - 3)]
        ind_a_max = bisect_right(nums4, target, 0, len(nums4))
        res = set()
        for ind1 in range(ind_a_min, ind_a_max):
            a = nums[ind1]
            ind_b_min = bisect_left(nums, target - a - nums[-1] - nums[-2], ind1 + 1, len(nums) - 3)
            nums3 = [nums[ind] + nums[ind + 1] + nums[ind + 2] for ind in range(0, len(nums) - 2)]
            ind_b_max = bisect_right(nums3, target - a, ind1 + 1, len(nums3))
            for ind2 in range(ind_b_min, ind_b_max):
                b = nums[ind2]
                ind_c_min = bisect_left(nums, target - a - b - nums[-1], ind2 + 1, len(nums) - 2)
                nums2 = [nums[ind] + nums[ind + 1] for ind in range(0, len(nums) - 1)]
                ind_c_max = bisect_right(nums2, target - a - b, ind2 + 1, len(nums2))
                for ind3 in range(ind_c_min, ind_c_max):
                    c = nums[ind3]
                    d_ind = bisect_left(nums, target - a - b - c, ind3 + 1)
                    if d_ind < len(nums) and nums[d_ind] == target -a - b - c:
                        res.add((a, b, c , nums[d_ind]))
        res = set(res)
        return list(res)


test = Solution()
A = [-1, 0, -5, -2, -2, -4, 0, 1, -2]
target = -9
res = test.fourSum(A, target)
print(res)
