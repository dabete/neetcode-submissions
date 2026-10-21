class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {")": "(",
                    "]": "[",
                    "}": "{"}
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                value = stack.pop()
                if dictionary[char] != value:
                    return False

        return len(stack) == 0