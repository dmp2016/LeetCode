class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        while num >= 1000:
            num -= 1000
            res += 'M'
        if 1000 > num >= 900:
            num -= 900
            res += 'CM'
        if 500 > num >= 400:
            num -= 400
            res += 'CD'
        if num >= 500:
            num -= 500
            res += 'D'
        while num >= 100:
            num -= 100
            res += 'C'
        if 100 > num >= 90:
            num -= 90
            res += 'XC'
        if 50 > num >= 40:
            num -= 40
            res += 'XL'
        if num >= 50:
            num -= 50
            res += 'L'
        while num >= 10:
            num -= 10
            res += 'X'
        if num == 9:
            num -= 9
            res += 'IX'
        if num == 4:
            num -= 4
            res += 'IV'
        if num >= 5:
            num -= 5
            res += 'V'
        while num > 0:
            num -= 1
            res += 'I'
        return res


test = Solution()
# print(test.intToRoman(num=3))
# print(test.intToRoman(num=4))
# print(test.intToRoman(num=9))
# print(test.intToRoman(num=58))
# print(test.intToRoman(num=1994))
# print(test.intToRoman(num=89))
# print(test.intToRoman(num=88))
# print(test.intToRoman(num=87))
# print(test.intToRoman(num=65))
print(test.intToRoman(num=40))


'''Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000'''

'''I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.'''