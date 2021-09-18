from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        num = list(map(int, num))
        ans = []
        opers = [0] * (len(num) - 1)
        while True:
            num1 = [num[0]]
            new_opers1 = []

            skip = False
            for oper, a in zip(opers, num[1:]):
                if oper == 0:
                    if num1[-1] == 0:
                        skip = True
                        break
                    num1[-1] = num1[-1] * 10 + a
                else:
                    new_opers1.append(oper)
                    num1.append(a)

            if not skip:
                num2 = [num1[0]]
                new_opers2 = []

                for oper, a in zip(new_opers1, num1[1:]):
                    if oper == 1:
                        num2[-1] *= a
                    else:
                        new_opers2.append(oper)
                        num2.append(a)
                
                res = num2[0]
                for oper, a in zip(new_opers2, num2[1:]):
                    if oper == 2:
                        res += a
                    else:
                        res -=a
                if res == target:
                    ans0 = str(num1[0])
                    for oper, a in zip(new_opers1, num1[1:]):
                        if oper == 1:
                            ans0 += '*'
                        elif oper == 2:
                            ans0 += '+'
                        else:
                            ans0 += '-'
                        ans0 += str(a)
                    ans.append(ans0)

            ind = 0
            while ind < len(opers):
                opers[ind] += 1
                if opers[ind] > 3:
                    opers[ind] = 0
                    ind += 1
                else:
                    break
            if ind == len(opers):
                break
        return ans


test = Solution()
# print(test.addOperators(num="123", target=6))
# print(test.addOperators(num="232", target=8))
# print(test.addOperators(num="105", target=5))
# print(test.addOperators(num="00", target=0))
# print(test.addOperators(num="3456237490", target=9191))
print(test.addOperators(num="123456789", target=45))