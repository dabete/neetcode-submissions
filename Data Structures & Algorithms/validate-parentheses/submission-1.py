class Solution:
    def isValid(self, s: str) -> bool:
        # input - string 's'
        
        stack = []
        open_brackets = "([{"
        close_brackets = ")]}"

        for character in s:
            if character in open_brackets:
                stack.append(character)

            elif character in close_brackets:
                if len(stack) == 0:
                    return False

                if character == ")":
                    popped = stack.pop()
                    if popped != "(":
                        return False

                if character == "]":
                    popped = stack.pop()
                    if popped != "[":
                        return False

                if character == "}":
                    popped = stack.pop()
                    if popped != "{":
                        return False

        return len(stack) == 0
            