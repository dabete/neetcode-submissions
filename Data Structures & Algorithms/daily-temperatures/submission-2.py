class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures = [30,38,30,36,35,40,28]
        # mono = [30, 30]
        res = [0]*len(temperatures)
        mono = []

        # next warmer day: 30,

        for i, temp in enumerate(temperatures):
            while len(mono) > 0 and temperatures[mono[-1]] < temp:
                value = mono.pop()
                res[value] = i - value # need to fix this 
            mono.append(i)

        return res

        

        





