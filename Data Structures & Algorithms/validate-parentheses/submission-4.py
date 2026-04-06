class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = []

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if len(stack) == 0 or brackets[stack.pop()] != char:
                    return False

        return len(stack) == 0