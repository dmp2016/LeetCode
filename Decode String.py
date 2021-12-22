class Solution:
    def decodeString(self, s: str) -> str:
        st = ['']
        state = 0
        for c in s:
            if c.isalpha():
                st[-1] += c
            elif c.isnumeric():
                if state != 1:
                    st.append('')
                    state = 1
                st[-1] += c
            elif c == '[':
                st[-1] = int(st[-1])
                st.append('')
                state = 0
            else:
                temp = st.pop()
                oper = int(st.pop())
                st[-1] += oper * temp
                state = 0
        return st[-1]


test = Solution()
print(test.decodeString(s="3[a]2[bc]"))
print(test.decodeString(s="3[a2[c]]"))
print(test.decodeString(s="2[abc]3[cd]ef"))
print(test.decodeString(s="abc3[cd]xyz"))
