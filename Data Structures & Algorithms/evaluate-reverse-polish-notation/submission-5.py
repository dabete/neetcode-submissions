class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # input - array of strings 'tokens'

        operators = "+-*/"

        stack = []

         
        # remember to check for minus

        for character in tokens:
            if character in operators:
                # we need to pop the stack twice
                value2 = stack.pop()
                value1 = stack.pop()

                if character == "+":
                    put_back = value1 + value2    
                if character == "-":
                    put_back = value1 - value2
                if character == "*":
                    put_back = value1 * value2
                if character == "/":
                    put_back = int(value1 / value2)

                stack.append(put_back)
            
            else:
                stack.append(int(character))


            
        return stack.pop()
