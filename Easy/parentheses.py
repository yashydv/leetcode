class Solution:
    def isValid(self, s: str) -> bool:
        table = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for w in s:
            if w in "{[(":
                stack.append(w)
            else:
                if stack == []:
                    return False
                test = stack.pop()
                if table[test] != w:
                    return False
        return stack == []
