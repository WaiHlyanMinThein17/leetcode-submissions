class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        opening = set("({[")
        stack = []

        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack[-1] == match[char]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0