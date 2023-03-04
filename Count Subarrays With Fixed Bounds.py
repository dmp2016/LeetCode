from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        def check_sub(sub_nums: List[int]) -> int:
            if not sub_nums:
                return 0
            res_sub = 0
            max_ind0 = None
            max_ind1 = 1
            while max_ind1 < len(sub_nums) and sub_nums[max_ind1] < maxK:
                max_ind1 += 1
            prev = -1

            for i in range(len(sub_nums)):
                if sub_nums[i] == maxK:
                    max_ind0 = i
                if sub_nums[i] == minK:
                    if max_ind1 < i:
                        max_ind1 = i + 1
                        while max_ind1 < len(sub_nums) and sub_nums[max_ind1] < maxK:
                            max_ind1 += 1

                    if max_ind0 is not None:
                        res_sub += (max_ind0 - prev) * (len(sub_nums) - i)
                        res_sub += (i - max_ind0) * (len(sub_nums) - max_ind1)
                    else:
                        res_sub += (i - prev) * (len(sub_nums) - max_ind1)
                    prev = i
                    max_ind0 = None

            return res_sub

        res = 0
        num_check = []
        for a in nums:
            if minK <= a <= maxK:
                num_check.append(a)
            else:
                res += check_sub(num_check)
                num_check.clear()
        
        res += check_sub(num_check)

        return res


test = Solution()
print(test.countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5))
print(test.countSubarrays(nums=[1, 1, 1, 1], minK=1, maxK=1))
print(test.countSubarrays(nums=[35054, 398719, 945315, 945315, 820417, 945315, 35054, 945315, 171832, 945315, 35054, 109750, 790964, 441974, 552913], minK=35054, maxK=945315))
print(test.countSubarrays(nums=[8121, 8121, 955792, 925378, 383928, 673920,
      457030, 925378, 925378, 925378, 92893, 456370, 925378], minK=8121, maxK=925378))
