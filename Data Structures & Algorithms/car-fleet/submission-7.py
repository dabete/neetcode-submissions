class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(zip(position, speed), reverse=True)
        stack = []
        fleet = 1

        for position, speed in ps:
            time = (target - position)/speed
            if len(stack) > 0 and stack[-1] < time:
                stack.append(time)
                fleet += 1
            if len(stack) == 0:
                stack.append(time)
                          
        return fleet 



        
        

        
        