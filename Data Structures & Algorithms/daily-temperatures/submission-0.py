class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # input - array of integers 'temperatures' 
        # what we need to do:
        # return an array 'result' where result[i] is the number of days after the ith day before a warmer temperature appears on a future day

        # requires monotonic stack

        stack = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)

        return result

        





