import re


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        nums = list(map(int, re.split('\+|\-|/|\*', s)))
        opers = re.split('\d+', s)[1:-1]
        new_opers = []
        new_nums = [nums[0]]
        ind_num = 1
        for oper in opers:
            if oper == '/':
                new_nums[-1] = new_nums[-1] // nums[ind_num]
            elif oper == '*':
                new_nums[-1] = new_nums[-1] * nums[ind_num]
            else:
                new_nums.append(nums[ind_num])
                new_opers.append(oper)
            ind_num += 1
        res = new_nums[0]
        ind_num = 1
        for oper in new_opers:
            if oper == '+':
                res += new_nums[ind_num]
            elif oper == '-':
                res -= new_nums[ind_num]
            ind_num += 1
        return res


test = Solution()
print(test.calculate("3+2*2"))
print(test.calculate(" 3/2 "))
print(test.calculate(" 3+5 / 2 "))
    