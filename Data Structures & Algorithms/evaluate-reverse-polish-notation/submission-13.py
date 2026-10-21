class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))

            else:
                rightValue = stack.pop()
                leftValue = stack.pop()
                if token == "+":
                    stack.append(leftValue + rightValue)
                elif token == "-":
                    stack.append(leftValue - rightValue)
                elif token == "/":
                    stack.append(int(leftValue / rightValue))
                elif token == "*":
                    stack.append(leftValue * rightValue)

        return stack[-1]