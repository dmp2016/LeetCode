class Solution:
    def simplifyPath(self, path: str) -> str:
        result = path[0]
        for c in path[1:]:
            if c == '/' and result[-1] == '/':
                continue
            else:
                result += c
        if result[-1] != '/':
            result += '/'
        while '/./' in result:
            result = result.replace('/./', '/')
        ind = result.find('/../')
        while ind >= 0:
            ind2 = ind + 4
            if ind > 0:
                ind -= 1
                while ind >= 0 and result[ind] != r'/':
                    ind -= 1
            result = result[:ind + 1] + result[ind2:]
            ind = result.find('/../')
        if len(result) > 1 and result[-1] == r'/':
            result = result[:-1]
        return result


test = Solution()
# print(test.simplifyPath(path="/home/"))
# print(test.simplifyPath(path="/../"))
# print(test.simplifyPath(path="/home//foo/"))
# print(test.simplifyPath(path="/a/./b/../../c/"))
# print(test.simplifyPath(path="/../../.."))
# print(test.simplifyPath(path="/../.../.."))
print(test.simplifyPath(path="/a//b////c/d//././/.."))
